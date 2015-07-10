# git-hooks
These are some git hooks used to ensure that tests are run, commit messages are in the proper format, etc.

##Client Hooks
All hooks that can be used on the developer/client side are described in this section and can be found in the client directory.

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

#####Story Status Types
Here is the list of accepted story status types:

- closes [also:  Closes, closed, Closed, CLOSES, CLOSED] - story/defect/issue is closed
- fixes [also:  Fixes, fixed, Fixed, FIXES, FIXED] - story/defect/issue is fixed
- wip [also: WIP] - story/defect/issue is being worked on, and commit should be associated with it
    

##Server Hooks
All hooks that can be used on the remote/server side are found in the server directory and are described here.

##Templates
All templates that can be used on the client side are found in the templates directory and are described here.

###commit-message-template
The commit-message-template provides a guide as the default message for git commits and matches the parameters set for
the commit-msg client hook, listed above.