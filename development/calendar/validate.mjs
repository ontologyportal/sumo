import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const sumo=path.resolve(here,'../..');
const sigma=process.env.SIGMA_RS_ROOT || path.resolve(sumo,'../sigma-rs');
const engine=await import(pathToFileURL(path.join(sigma,'packages/sigmakee/dist/engine.js')));
engine.initSync({module:fs.readFileSync(path.join(sigma,'packages/sigmakee/dist/engine_bg.wasm'))});
const s=new engine.Session();
console.log('Merge.kif load diagnostics:',s.loadKif(fs.readFileSync(path.join(sumo,'Merge.kif'),'utf8'),'Merge.kif'));
const baseline=s.validate();
const files=['DateTime.kif','DateTime-benchmarks.kif'];
for(const file of files){
 const errors=s.loadKif(fs.readFileSync(path.join(here,file),'utf8'),file);
 if(errors.length)throw new Error(JSON.stringify(errors));
}
const diagnostics=s.validate().filter(d=>files.includes(d.file));
const counts={};
for(const d of diagnostics){const key=d.severity+'/'+d.code;counts[key]=(counts[key]||0)+1;}
const report={background:'Merge.kif',baselineDiagnostics:baseline.length,counts,diagnostics};
fs.writeFileSync(path.join(here,'validation.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(counts,null,2));
if(diagnostics.some(d=>d.severity==='error'))process.exitCode=1;
if(diagnostics.some(d=>d.severity==='warning' && !(d.code==='missing-arity' && /'(DateTimeMinuteIntervalFn|DateTimeFromYMDHMFn)'/.test(d.message))))process.exitCode=1;
