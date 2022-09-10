function browserHistory (browserObj, arrActions) {

    for (let el of arrActions) {
        if (el === "Clear History and Cache") {
            browserObj["Open Tabs"] = [];
            browserObj["Recently Closed"] = [];
            browserObj["Browser Logs"] = [];
        } else {
            let tokens = el.split(' ');
            let action = tokens.shift();
            let site = tokens.join(' ');
            
            if (action === "Open") {
                browserObj["Open Tabs"].push(site);
                browserObj["Browser Logs"].push(el);
            } else if (action === "Close" && browserObj["Open Tabs"].includes(site)) {
                let index = browserObj["Open Tabs"].indexOf(site);
                browserObj["Open Tabs"].splice(index, 1);
                browserObj["Recently Closed"].push(site);
                browserObj["Browser Logs"].push(el);
            }
        }
    }

    console.log(`${browserObj["Browser Name"]}\nOpen Tabs: ${browserObj["Open Tabs"].join(', ')}\nRecently Closed: ${browserObj["Recently Closed"].join(', ')}\nBrowser Logs: ${browserObj["Browser Logs"].join(', ')}`);

}

browserHistory({"Browser Name":"Google Chrome","Open Tabs":["Facebook","YouTube","Google Translate"],
"Recently Closed":["Yahoo","Gmail"],
"Browser Logs":["Open YouTube","Open Yahoo","Open Google Translate","Close Yahoo","Open Gmail","Close Gmail","Open Facebook"]},
["Close Facebook", "Open StackOverFlow", "Open Google"]);