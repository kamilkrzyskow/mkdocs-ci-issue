# Test Page 1

Uses [https://squidfunk.github.io/mkdocs-material/getting-started/](https://squidfunk.github.io/mkdocs-material/getting-started/)

## Another heading

Some text


## Codeblock
Some `code`

```lua
local test = "test"
```

```lua title="Title Test"
-- Comment test
local test = 123
local test2 = 1 + 1

function test()

end

local test3 = {
	["test"] = {}
}

function test3.func1() end
function test3.a.b.cfunc1() end

test3.func1()
test3.func1

test4.a.b.c
```


#### test
{{client-only}} {{server-only}} {{deprecated}}

```lua
function test(a, b)
```

<args>
    <arg name="arg1" type="string">The first argument.</arg>
    <arg name="arg2" type="string">The second argument.</arg>
</args>

<rets>
    <ret name="" type="nil">Nothing</ret>
</rets>

## Another heading

More text


!!! note
    This is a test


!!! info "Test"
    test

??? note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!! info inline end "Inline test"
    test

Text can be {--deleted--} and replacement text {++added++}. This can also be
combined into {~~one~>a single~~} operation. {==Highlighting==} is also
possible {>>and comments can be added inline<<}.

{==

Formatting can also be applied to blocks by putting the opening and closing
tags on separate lines and adding new lines between the tags and the content.

==}

<div class="grid" markdown>
Test
{ .card }

Test2
{ .card }

Test3
{ .card }

>Test4
{ .card }
</div>

=== "Test"
    test
=== "Test2"
    test2

``` mermaid
graph LR
  A[Start] --> B{Error?};
  B -->|Yes| C[Hmm...];
  C --> D[Debug];
  D --> B;
  B ---->|No| E[Yay!];
```

:thinking:

- [x] Lorem ipsum dolor sit amet, consectetur adipiscing elit
- [ ] Vestibulum convallis sit amet nisi a tincidunt
    * [x] In hac habitasse platea dictumst
    * [x] In scelerisque nibh non dolor mollis congue sed et metus
    * [ ] Praesent sed risus massa
- [ ] Aenean pretium efficitur erat, donec pharetra, ligula non scelerisque

<br>
<br>
<br>
<br>
<br>