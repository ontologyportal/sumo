import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const sumo=path.resolve(here,'../..');
const sigma=process.env.SIGMA_RS_ROOT || path.resolve(sumo,'../sigma-rs');
const engine=await import(pathToFileURL(path.join(sigma,'packages/sigmakee/dist/engine.js')));
engine.initSync({module:fs.readFileSync(path.join(sigma,'packages/sigmakee/dist/engine_bg.wasm'))});
const s=new engine.Session();
const background=s.loadKif(fs.readFileSync(path.join(sumo,'Merge.kif'),'utf8'),'Merge.kif');
const baseline=s.validate();
const dateTime=fs.readFileSync(path.join(sumo,'DateTime.kif'),'utf8');
const errors=s.loadKif(dateTime,'DateTime.kif');
if(errors.length)throw new Error(JSON.stringify(errors));
const diagnostics=s.validate().filter(d=>d.file==='DateTime.kif');
console.log('DateTime errors/warnings:',JSON.stringify(diagnostics.filter(d=>['error','warning'].includes(d.severity))));
// Count literals in emitted CNF, so a passing test run cannot conceal clauses
// discarded by the native prover's default length limit.
function literalCount(clause) {
 const tokens=clause.match(/"(?:\\.|[^"\\])*"|[()]|[^\s()]+/g);
 let at=0;
 function read() {
  const token=tokens[at++];
  if(token!=='(')return token;
  const result=[];
  while(tokens[at]!==')')result.push(read());
  at++;
  return result;
 }
 const root=read();
 return Array.isArray(root) && root[0]==='or' ? root.length-1 : 1;
}
const clauses=s.clausify(dateTime);
const maxClauseLiterals=Math.max(0,...clauses.map(literalCount));
const cfg=new engine.Config();cfg.timeLimitSecs=5;cfg.maxSteps=5000;s.configure(cfg);
if(maxClauseLiterals>cfg.maxLits)throw new Error(`Clause length ${maxClauseLiterals} exceeds default ${cfg.maxLits}`);
console.log(`DateTime CNF: ${clauses.length} clauses; max ${maxClauseLiterals} literals (default limit ${cfg.maxLits}).`);
const results=[];
for(const file of fs.readdirSync(here).filter(f=>f.endsWith('.kif.tq') && (!process.argv[2] || f===process.argv[2])).sort()){
 const tc=engine.parseTest(file,fs.readFileSync(path.join(here,file),'utf8'));
 const support=s.tell(tc.axiomKif,file);
 if(!support.ok || support.errors.length)throw new Error(file+': '+JSON.stringify(support));
 const start=Date.now();const r=s.ask(tc.queryKif,file);
 const result={file,status:r.status,proved:r.proved,steps:r.given_steps,elapsedMs:Date.now()-start};
 results.push(result);console.log(JSON.stringify(result));
}
for(const lang of ['fof','tff'])console.log(lang+' export bytes: '+s.toTptpIndexed(lang,false).length);
const report={backgroundLoadDiagnostics:background,baselineDiagnosticCount:baseline.length,clauseCount:clauses.length,maxClauseLiterals,diagnostics,results};
if(!process.argv[2])fs.writeFileSync(path.join(here,'validation.json'),JSON.stringify(report,null,2)+'\n');
if(diagnostics.some(d=>['error','warning'].includes(d.severity)) || results.some(r=>!r.proved))process.exitCode=1;
