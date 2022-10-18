function requestValidator(request) {
    const validRequest = ['GET', 'POST', 'DELETE', 'CONNECT'];
    const validVersion = ['HTTP/0.9', 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0'];

    const validUriRegEx = /(\*)|^([\.A-Za-z\d]+)$/gm;
    const validMessageRegEx = /^$|^([^\<\>\\\&\'\""]+)$/gm;

    if (!request.hasOwnProperty('method') || !validRequest.includes(request['method'])) {
        throw new Error('Invalid request header: Invalid Method');
    } else if (!request.hasOwnProperty('uri') || !request['uri'].match(validUriRegEx)) {
        throw new Error('Invalid request header: Invalid URI');
    } else if (!request.hasOwnProperty('version')|| !validVersion.includes(request['version'])) {
        throw new Error('Invalid request header: Invalid Version');
    } else if (!request.hasOwnProperty('message') || !request['message'].match(validMessageRegEx)) {
        throw new Error('Invalid request header: Invalid Message');
    }

    return request
}


// console.log(requestValidator({
//     method: 'GET',
//     uri: 'svn.public.catalog',
//     version: 'HTTP/1.1',
//     message: ''
//   }));

// console.log(requestValidator({
//     method: 'OPTIONS',
//     uri: 'git.master',
//     version: 'HTTP/1.1',
//     message: '-recursive'
//   }));

// console.log(requestValidator({
//     method: 'POST',
//     uri: 'git.master$',
//     version: 'HTTP/1.1',
//     message: '-recursive'
//   }));

console.log(requestValidator({
    method: 'POST',
    uri: 'git.master',
    version: 'HTTP/1.12',
    message: '-recursive'
}));