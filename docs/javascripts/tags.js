var templateTags = [
    ["{{client-only}}", '<span class="tag client-only">client-only</span>'],
	["{{server-only}}", '<span class="tag server-only">server-only</span>'],
	["{{deprecated}}", '<span class="tag deprecated">deprecated</span>'],
];

function replace(element, from, to) {
    if (element.nodeType === Node.TEXT_NODE) {
        const cont = element.textContent;
        if (cont && cont.includes(from)) {
            const parts = cont.split(from);
            const newElement = document.createElement("span");
            newElement.innerHTML = to;

            element.replaceWith(...parts.flatMap((part, index, array) => index === array.length - 1
                ? [document.createTextNode(part)]
                : [document.createTextNode(part), newElement.cloneNode(true)]
            ));
        }
    } else if (element.childNodes.length) {
        element.childNodes.forEach(child => replace(child, from, to));
    }
}

// Replace stuff
templateTags.forEach(function(item) {
    replace(document.body, item[0], item[1]);
})