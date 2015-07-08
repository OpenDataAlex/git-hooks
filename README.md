# git-hooks
These are some git hooks used to ensure that tests are run, commit messages are in the proper format, etc.

##client hooks
All hooks that can be used on the developer/client side are found here.

###commit-msg
Based on the commit message convention created by [AngularJS](https://github.com/angular/angular.js/blob/master/CONTRIBUTING.md#commit).
If the commit message does not meet the format, the hook will fail the commit and let the committer know why.

####Commit Message Format

    <type>(<scope>): <subject>
    <BLANK LINE>
    <body>
    <BLANK LINE>
    <breaks>
    <BLANK LINE>
    <stories>

The commit message format is simple to use, starting with the type of work being done (type), where the work is applied
 (scope), followed by a short 50 character subject.  The body should describe why the changes are being made.  The 
 breaks section should describe anything that may break backwards compatibility for the code base. The stories section 
 should list the stories/defects/issues either being worked on or closed.
 
#####Example

The following is a back of the napkin example:

    feat(NewFeature): create new feature
    
    Made change to include new functionality.  Had to use X over Y because the library did not end up 
    supporting the requested feature as planned.
    
    Breaks:  N/A
        
    Closed #12345, WIP: #12346

#####Types
Here is the list of accepted types:

- feat: A new feature
- fix: A bug fix
- docs: Documentation only changes
- style: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- refactor: A code change that neither fixes a bug or adds a feature
- perf: A code change that improves performance
- test: Adding missing tests
- chore: Changes to the build process or auxiliary tools and libraries such as documentation generation
    

##server hooks
All hooks that can be used on the remote/server side are found here.
