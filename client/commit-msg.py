#!/usr/bin/env python
"""
Git commit hook:
 .git/hooks/commit-msg
Based on the gist found at:  https://gist.github.com/onjin/5442494, originally created by Onjin
"""
__author__ = 'ameadows'

import sys
import re

valid_commit_types = ['feat', 'FEAT', 'FEATURE', 'feature',
                      'fix', 'FIX',
                      'docs', 'DOCS', 'documentation', 'DOCUMENTATION',
                      'style', 'STYLE',
                      'refactor', 'REFACTOR',
                      'test', 'TEST',
                      'chore', 'CHORE', ]

valid_status_types = ['closes', 'Closes', 'closed', 'Closed',
                      'fixes', 'Fixes', 'fixed', 'Fixed',
                      'wip', 'WIP', ]



break_section_regex = '^[B|b]reaks'

story_type_regex = '^(([Cc]lose[ds]|CLOSE[DS])|([Ff]ixe[ds]|FIXE[DS])|(WIP|wip))'

commit_file = sys.argv[1]
#commit_file = "../test/test_files/message_file_bad.txt"

help_address = 'https://github.com/OpenDataAlex/git-hooks/blob/master/README.md'
commit_errors = []

with open(commit_file) as commit:
    lines = commit.readlines()
    if len(lines) == 0:
        commit_errors.append("[POLICY] Empty commit message not allowed\n")

    # first line
    line = lines[0]

    # Need to test that the subject line matches the "type(scope): subject" format
    m = re.search('^(.*)\((.*)\): (.*)$', line)

    if not m or len(m.groups()) != 3:
        commit_errors.append("[POLICY] First commit message line (header) does not follow format: type(scope): "
                             "message\n")

    else:
        commit_type, commit_scope, commit_message = m.groups()
        if commit_type not in valid_commit_types:
            commit_errors.append("[POLICY] Commit type not in list of valid commit types: %s\n" % ", "
                                 .join(valid_commit_types))

        if len(lines) > 1 and lines[1].strip():
            commit_errors.append("[POLICY] Second commit message line must be empty\n")

        if len(lines) > 2 and not lines[2].strip():
            commit_errors.append("[POLICY] Third commit message line (body) must not be empty\n")

        # Start count at 3 because the first lines are already processes above.
        count = 3

        # Adding flags to check for other sections of the commit message.
        breaks_section = False
        story_section = False

        # Due to an indeterminate number of lines that could occur, we need to use a while loop to test
        # the line logic.
        while count <= len(lines) - 1:

            cur_line = lines[count].strip()

            # Finding the break section.  This is an optional section since not every commit will break something.
            if re.search(break_section_regex, cur_line):
                breaks_section = True
                if lines[count-1].strip():
                    commit_errors.append("[POLICY] Line after message body and before breaks section must be empty\n")
                    print(lines[count-1].strip())

            # Finding the story section.  This section is required as every commit will have stories/defects associated.
            if re.search(story_type_regex, cur_line):
                story_section = True

                if lines[count-1].strip() and not re.search(story_type_regex, lines[count-1].strip()):
                    commit_errors.append("[POLICY] Line after message body/breaks section and before story section"
                                         " must be empty\n")

            count += 1

    if not story_section:
        commit_errors.append("[POLICY] Stories/defects must be listed with their status as part of the commit message. "
                             "Valid status types are: %s\n" % ", "
                                 .join(valid_status_types))

if commit_errors:
    for error in commit_errors:
        sys.stderr.write(error)
    sys.stderr.write("\n - Refer commit guide: %s\n\n" % help_address)
    sys.exit(1)

sys.exit(0)
