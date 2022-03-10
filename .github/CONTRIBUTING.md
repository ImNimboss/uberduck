## Contributing to Uberduck

First off, thanks for taking the time to contribute. It makes the library substantially better :+1:

The following is a set of guidelines for contributing to the repository. These are guidelines, not hard rules.

## This is too much to read! I want to ask a question!

Generally speaking questions are better suited in our resources below.

- [The official support server](https://discord.gg/FcxqdJ7AQq)
- [The FAQ in the documentation](https://github.com/ImNimboss/uberduck/blob/main/Documentation/FAQ.md)

Please try your best not to ask questions in our issue tracker. Most of them don't belong there unless they provide value to a larger audience.

## Good Bug Reports

Please be aware of the following things when filing bug reports.

1. Don't open duplicate issues. Please search your issue to see if it has been asked already. Duplicate issues will be closed.
2. When filing a bug about exceptions or tracebacks, please include the *complete* traceback. Without the complete traceback the issue might be **unsolvable** and you will be asked to provide more information.
3. Make sure to provide enough information to make the issue workable. The issue template will generally walk you through the process but they are enumerated here as well:
    - A **summary** of your bug report. This is generally a quick sentence or two to describe the issue in human terms.
    - Guidance on **how to reproduce the issue**. Ideally, this should have a small code sample that allows us to run and see the issue for ourselves to debug. **Please make sure that any bot tokens are not displayed**. If you cannot provide a code snippet, then let us know what the steps were, how often it happens, etc.
    - Tell us **what you expected to happen**. That way we can meet that expectation.
    - Tell us **what actually happens**. What ends up happening in reality? It's not helpful to say "it fails" or "it doesn't work". Say *how* it failed, do you get an exception? Does it hang? How are the expectations different from reality?
    - Tell us **information about your environment**. What version of Uberduck are you using? How was it installed? What operating system are you running on? These are valuable questions and information that we use.

If the bug report is missing this information then it'll take us longer to fix the issue. We will probably ask for clarification, and barring that if no response was given then the issue will be closed.

## Submitting a Pull Request

Submitting a pull request is fairly simple, just make sure it focuses on a single aspect and doesn't manage to have [scope creep](https://www.projectmanagementqualification.com/blog/2019/03/07/manage-scope-creep/) and it's probably good to go. It would be incredibly lovely if the style is consistent to that found in the project.

### Git Commit Guidelines

- Use present tense (e.g. "Add feature" not "Added feature")
- Reference issues or pull requests outside of the first line.
    - Please use the shorthand `#123` and not the full URL.
- There's no strict limit on line length as long as the line is readable.

If you do not meet any of these guidelines don't fret, but please do try to meet them to remove some of the workload.

## CONTRIBUTING.md credits - [The discord.py repository](https://github.com/Rapptz/discord.py)