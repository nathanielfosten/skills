# Contributing

Add a skill by copying the template, generalizing it, and listing it in the README.

## Add a skill

1. Copy the template and rename the directory in kebab-case:

   ```bash
   cp -R skills/_template skills/your-skill-name
   ```

   The `name` in `SKILL.md` must match that directory exactly: lowercase letters, numbers, and hyphens, 64 characters or fewer, no leading, trailing, or doubled hyphen.

2. Rewrite `description` as trigger text. Say what the skill does and when to use it, in the third person. Agents see this before they see the rest of the file.

3. Replace the template guidance. Keep the skill to one job, and keep `SKILL.md` short. Put sample input and output in `examples/`, and longer reference in `references/` only if the body would be worse for including it.

4. Add a row to the index in [README.md](README.md): name, one-line description, link.

5. Check the frontmatter:

   ```bash
   python3 scripts/validate_skills.py
   ```

The same check runs on pull requests.

## Generalize a skill that came from work

A skill written on a real project is not ready to publish until a stranger could use it. Walk this list before opening a pull request:

- [ ] Remove company, team, and product names
- [ ] Remove internal URLs, ticket ids, and private hostnames
- [ ] Remove proprietary component and token names. Describe the role ("the primary button", "the spacing scale") instead of the internal one
- [ ] Remove secrets, customer data, and unreleased work
- [ ] Rewrite examples so they stand alone, with no assumed codebase
- [ ] Read it once as if you had never seen the original project

If a step only makes sense inside one company, cut it or rewrite it until it doesn't.
