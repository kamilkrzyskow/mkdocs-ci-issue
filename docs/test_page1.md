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


## Another heading

More text


!!! note
    This is a test


!!! note "Test"
    test

??? note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!! info inline end "Inline test"
    test

``` mermaid
graph LR
  A[Start] --> B{Error?};
  B -->|Yes| C[Hmm...];
  C --> D[Debug];
  D --> B;
  B ---->|No| E[Yay!];
```

<br>
<br>
<br>
<br>
<br>