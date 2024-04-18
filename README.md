# <p align="center">🪼 Jellyfish 🪼</p>

<p align="center">
    <a href="https://github.com/codereport/jellyfish/issues" alt="contributions welcome">
        <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" /></a>
    <a href="https://lbesson.mit-license.org/" alt="MIT license">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" /></a>
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/Python-3-ff69b4.svg"/></a>
    <a href="https://github.com/codereport?tab=followers" alt="GitHub followers">
        <img src="https://img.shields.io/github/followers/codereport.svg?style=social&label=Follow" /></a>
    <a href="https://GitHub.com/codereport/jellyfish/stargazers/" alt="GitHub stars">
        <img src="https://img.shields.io/github/stars/codereport/jellyfish.svg?style=social&label=Star" /></a>
    <a href="https://twitter.com/code_report" alt="Twitter">
        <img src="https://img.shields.io/twitter/follow/code_report.svg?style=social&label=@code_report" /></a>
</p>

Jellyfish is an extension of the [Jelly programming language](https://github.com/DennisMitchell/jellylanguage/) created by Dennis Mitchell. Please visit his [repo](https://github.com/DennisMitchell/jellylanguage/) for the original documentation. This repo will focus on fixes and extensions as well as additional documention when I think it may be helpful.

Note that the primary way I interact with Jelly(fish) is through the Jello REPL. This allows you to write Jello keywords instead of Jelly atoms. It also visually diagrams the combinator trees that are implicitly created from the monadic, dyadic and multichains. You can find the [Jello repo here](https://github.com/codereport/jello/).

## Installing

```bash
git clone -q https://github.com/codereport/jellyfish.git
cd jellyfish
pip3 install --upgrade --user .
```

## Using

The intended way of using Jellyfish is through the [Jello REPL](https://github.com/codereport/jello/).

## Differences

### Additions

#### Atoms

* `ṕ` (Q's `prior`)
* `É` (dual to `odd?` i.e. `even?`)
* `①` (`bits` aka `bit_count`, `pop_count` or `ones_count`)
* `ḳ` (Uiua's `keep` and BQN/APL's `compress`/`replicate`)
* `Ḿ` (Q's `maxs`)
* `Ṕ` (Uiua's `partition` - we are calling it `part`)
* `Ꝑ` (adding `part_by` - a generalization of `part`)
* `≤` (less than equal to)
* `≥` (greater than equal to)
* `Œɠ` (previously `group_len`, this is a quick similar to `key`)

#### Chains

* `D₂`: previously spelled `l f₁ : g₂ : r h₁` and now `g₂ f₁ h₁`

### Changes

* `Ḣ`: `head` does not modify the underlying sequence
* `Ṫ`: `last` does not modify the underlying sequence
* `ÐṀ`: `max_by` returns a single value instead of list

### Deletions
* `Œɠ`: delete `group_len`; it can now be spelled `len group`

### Fixes

* `Ẓ`: isprime was broken, now fixed
