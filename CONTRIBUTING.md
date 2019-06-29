# Contributing

By participating in this project, you agree to abide by the [code of conduct](#code-of-conduct).

## Issues

One of the easiest ways to contribute is to log an issue. The most important issue is where
you may have found a logical contradiction with a theorem prover.  In that case, please provide

* the proof of the issue
* the exact SUMO files you provided to the prover
* the command line invocation of the prover
* the version of the prover

Please note that often people will casually say that some axiom is wrong but not provide
a proof showing how it is wrong.  Such reports are not helpful and can actually detract
from time spent on the project.

If you're making changes to add reasoning functionality, instead of eliminate a contradiction, it's
very helpful to show a proof of some new conclusion that is enabled.

Other useful reports are for things like a misspelled variable that doesn't result
in a contradiction, or a typo in a documentation string.

## Additions

If you want to add content to SUMO, please note that it is a theory in an expressive
logic and more than just a taxonomy or simple frame-slot assertions are expected.
For more guidelines, please see what to do to write an addition - 
http://www.adampease.org/OP/Process.html
and things to avoid - http://www.adampease.org/OP/Pitfalls.html

## Pull Requests

We love pull requests from everyone. 

git close https://github.com/ontologyportal/sumo

Some things that will increase the chance that your pull request is accepted:

* Make small incremental changes.
* Avoid the use of automatic tools or formatters to keep commits small and trackable.
* Write a [good commit message][commit].
* explain (ideally with an automated proof) what your addition attempts to accomplish,
which could be information that would support automated reasoning in a new domain

[commit]: http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html

## Code of conduct

In order to foster an inclusive, kind, harassment-free, and cooperative community, we enforce this code of conduct on our open source projects.

### Summary

Harassment in code and discussion or violation of physical boundaries is completely unacceptable anywhere in our project. Violators will be warned by the core team. Repeat violations will result in being blocked or banned by the core team at or before the 3rd violation.

### In detail

Harassment includes offensive verbal comments related to gender identity, gender expression, sexual orientation, disability, physical appearance, body size, race, religion, sexual images, deliberate intimidation, stalking, sustained disruption, and unwelcome sexual attention.

Individuals asked to stop any harassing behavior are expected to comply immediately.

Maintainers are also subject to the anti-harassment policy.

If anyone engages in harassing behavior, including maintainers, we may take appropriate action, up to and including warning the offender, deletion of comments, removal from the project’s codebase and communication systems, and escalation to GitHub support.

If you are being harassed, notice that someone else is being harassed, or have any other concerns, please contact us immediately

We expect everyone to follow these rules anywhere in our project.

Finally, don't forget that it is human to make mistakes! We all do. Let’s work together to help each other, resolve issues, and learn from the mistakes that we will all inevitably make from time to time.

### Thanks
Derived from [thoughbot's code of conduct](https://thoughtbot.com/open-source-code-of-conduct)
