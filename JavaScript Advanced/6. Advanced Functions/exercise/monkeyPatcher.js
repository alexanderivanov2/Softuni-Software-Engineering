function solution(action) {
    
    if (action == 'upvote') {
        return this.upvotes += 1;
    } else if(action == 'downvote') {
        return this.downvotes += 1;
    } else if (action == 'score') {

        let bonusVotes = Math.ceil(Math.max(this.upvotes, this.downvotes) * 0.25);
        let totalVotes = this.downvotes + this.upvotes;
        let balance = this.upvotes - this.downvotes;

        let inflatedUpvotes = this.upvotes;
        let inflatedDownvotes = this.downvotes;

        if (totalVotes > 50) {
            inflatedDownvotes += bonusVotes;
            inflatedUpvotes += bonusVotes;
        }

        let rating = 'new';

        if (totalVotes < 10) {
            rating = 'new';
        } else if (this.upvotes > totalVotes * 0.66) {
            rating = 'hot';
        } else if (totalVotes > 100 && balance >= 0) {
            rating = 'controversial';
        } else if (balance < 0) {
            rating = 'unpopular';
        }

        return [inflatedUpvotes, inflatedDownvotes, balance, rating]
    }
}

let post = {
    id: '3',
    author: 'emil',
    content: 'wazaaaaa',
    upvotes: 100,
    downvotes: 100
};
solution.call(post, 'upvote');
solution.call(post, 'downvote');
let score = solution.call(post, 'score');
console.log(score);
for (let i = 1; i <= 50; i++) {
    solution.call(post, 'upvote'); 
}   
        // (executed 50 times)
score = solution.call(post, 'score');
console.log(score);
// var forumPost = {
//     id: '1',
//     author: 'pesho',
//     content: 'hi guys',
//     upvotes: 0,
//     downvotes: 0
// };

// solution.call(forumPost, 'downvote');

// var answer = solution.call(forumPost, 'score');
// var expected = [1, 0, 1, 'new'];

// console.log(answer)

// compareScore(expected, answer);

// function compareScore(expected, answer) {
//     expect(expected[0]).to.equal(answer[0], 'Incorrect number of upvotes');
//     expect(expected[1]).to.equal(answer[1], 'Incorrect number of downvotes');
//     expect(expected[2]).to.equal(answer[2], 'Incorrect score');
//     expect(expected[3]).to.equal(answer[3], 'Incorrect rating');
// }