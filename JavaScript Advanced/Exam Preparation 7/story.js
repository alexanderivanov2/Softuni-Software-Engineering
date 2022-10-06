class Story {
    constructor(title, creator) {
        this.title = title;
        this.creator = creator;
        this._comments = [];
        this._likes = [];
        
    }

    // get title() {
    //     return this._title;        
    // }

    // set title(value) {
    //     this._title = value;
    // }

    // get creator() {
    //     return this._creator;
    // }

    // set creator(value) {
    //     this._creator = value;
    // }

    get likes() {
        const likesNum = this._likes.length;

        if(likesNum == 0) {
            return `${this.title} has 0 likes`;
        }

        if (likesNum == 1) {
            return `${this._likes[0]} likes this story!`;
        }

        return `${this._likes[0]} and ${likesNum - 1} others like this story!`;
    }


    like(username) {
        if (this._likes.includes(username)) {
            throw new Error(`You can't like the same story twice!`);
        }

        if (this.creator == username) {
            throw new Error(`You can't like your own story!`)
        }

        // this.likesUsername.push(username);
        this._likes.push(username);
        return `${username} liked ${this.title}!`
    }

    dislike(username) {
        if (!this._likes.includes(username)) {
            throw new Error(`You can't dislike this story!`)
        }

        this._likes = this._likes.
            filter(user => user != username);
        // console.log(this.likesUsername)

        return `${username} disliked ${this.title}`
    }

    comment(username, content, id) {
        const comment = this._comments.find(el => el['id'] == id);

        if (comment) {
            const replyId = `${id}.${comment.replies.length + 1}`;
            comment.replies.push({id: replyId, username, content});
            return `You replied successfully`;
        }

        id = this._comments.length + 1;
        this._comments.push({id, username, content, replies: []});
        return `${username} commented on ${this.title}`
    }

    toString(sortingType) {
        const result = [`Title: ${this.title}`, `Creator: ${this.creator}`, `Likes: ${this._likes.length}`, 'Comments:'];

        let sortComments = this.sortingElements(this._comments, sortingType);

        // if (sortingType == 'asc') {
        //    sortComments = this._comments.sort((a, b) => a.id - b.id); 
        // } else if (sortingType == 'desc') {
        //     sortComments = this._comments.sort((a,b) => b.id - a.id);
        // } else if (sortingType == 'username') {
        //     sortComments = this._comments.sort((a, b) => a.username.localeCompare(b.username));
        // }
        // sortComments = this.comments.sort((a, b) => a.id - b.id); 
        // console.log(this.comments);

        for (let comment of sortComments) {
            const replies = comment.replies;
            result.push(`-- ${comment.id}. ${comment.username}: ${comment.content}`)
            if (replies.length > 0) {
                let sortReplies = this.sortingElements(replies, sortingType);
                for (let el of sortReplies) {
                    result.push(`--- ${el.id}. ${el.username}: ${el.content}`);
                }
            }
        }


        return result.join('\n');
    }

    sortingElements(element, sortingType) {
        let sortElements;
        if (sortingType == 'asc') {
            sortElements = element.sort((a, b) => a.id - b.id); 
        } else if (sortingType == 'desc') {
            sortElements = element.sort((a, b) => b.id - a.id);
        } else if (sortingType == 'username') {
            sortElements = element.sort((a, b) => a.username.localeCompare(b.username));
        }
        
        return sortElements;
    }
}


// const replie = comment.find(el => id);

let art = new Story("My Story", "Anny");
// console.log(art);
console.log(art.likes)
art.like("John");
console.log(art.likes);
art.dislike("John");
console.log(art.likes);
console.log(art);
art.comment("Sammy", "Some Content");
console.log(art.comment("Ammy", "New Content"));
art.comment("Zane", "Reply", 1);
art.comment("Jessy", "Nice :)");
console.log(art.comment("SAmmy", "Reply@", 1));
console.log()
console.log(art.toString('username'));
console.log()
art.like("Zane");
console.log(art.toString('desc'));


// Unexpected error: expected 'Title: My Story\nCreator: Anny\nLikes: 0\nComments:\n-- 1. Anny: Some Content\n--- 1.1. Ammy: New Content\n-- 2. Zane: Reply\n--- 2.1. SAmmy: Reply@\n-- 3. Jessy: Nice :)' to equal 'Title: My Story\nCreator: Anny\nLikes: 3\nComments:\n-- 1. Anny: Some Content\n--- 1.1. Ammy: New Content\n-- 2. Zane: Reply\n--- 2.1. SAmmy: Reply@\n-- 3. Jessy: Nice :)'