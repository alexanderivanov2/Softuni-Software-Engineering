class ArtGallery {
    constructor(creator) {
        this.creator = creator;
        this.possibleArticles = { "picture":200,"photo":50,"item":250 };
        this.listOfArticles = [];
        this.guests = [];
    }

    addArticle(articleModel, articleName, quantity) {
        articleModel = articleModel.toLowerCase();
        if (!this.possibleArticles.hasOwnProperty(articleModel.toLowerCase())) {
            throw new Error('This article model is not included in this gallery!');
        }

        let findArticle = this.listOfArticles.find(a => a.articleName == articleName && a.articleModel == articleModel);
        if (findArticle) {
            findArticle.quantity += quantity;
        } else {
            this.listOfArticles.push({articleModel: articleModel, articleName: articleName, quantity: quantity});
        }

        return `Successfully added article ${articleName} with a new quantity- ${quantity}.`;
    }

    inviteGuest(guestName, personality) {
        let findGuest = this.guests.find(guest => guest.guestName == guestName);

        if (findGuest) {
            throw new Error(`${guestName} has already been invited.`);
        } 
        
        let personalityPts = {'Vip': 500, 'Middle': 250};
        let points = personalityPts.hasOwnProperty(personality) ? personalityPts[personality] : 50;
        this.guests.push({guestName:guestName, 'points':points, purchaseArticle: 0});
        
        return  `You have successfully invited ${guestName}!`;
    }

    buyArticle(articleModel, articleName, guestName) {
        articleModel = articleModel.toLowerCase();
        let findArticle = this.listOfArticles.find(article => article.articleName == articleName && article.articleModel == articleModel);
        let findGuest = this.guests.find(guest => guest.guestName == guestName);

        if (!findArticle) {
            throw new Error('This article is not found.');
        } else if(findArticle.quantity == 0){
            return `The ${articleName} is not available.`;
        } else if(!findGuest) {
            return 'This guest is not invited.';
        }

        if (this.possibleArticles[articleModel] > findGuest.points) {
            return 'You need to more points to purchase the article.';
        }

        findArticle.quantity -= 1;
        findGuest.points -= this.possibleArticles[articleModel];
        findGuest.purchaseArticle += 1;
        return `${guestName} successfully purchased the article worth ${this.possibleArticles[articleModel]} points.`;
    }

    showGalleryInfo(criteria) {
        let result = [];
        if (criteria == 'article') {
            result.push('Articles information:');
            this.listOfArticles.forEach(article => {
                result.push(`${article.articleModel} - ${article.articleName} - ${article.quantity}`);
            });
        } else if (criteria == 'guest') {
            result.push('Guests information:');
            this.guests.forEach(guest => {
                result.push(`${guest.guestName} - ${guest.purchaseArticle}`);
            })
        }

        return result.join('\n');
    }
}

const artGallery = new ArtGallery('Curtis Mayfield');
console.log(artGallery.addArticle('picture', 'Mona Liza', 3));
console.log(artGallery.addArticle('Item', 'Ancient vase', 2));
console.log(artGallery.addArticle('picture', 'Mona Liza', 1));
console.log(artGallery.inviteGuest('John', 'Vip'));
console.log(artGallery.inviteGuest('Peter', 'Middle'));
console.log(artGallery.buyArticle('picture', 'Mona Liza', 'John'));
console.log(artGallery.buyArticle('item', 'Ancient vase', 'Peter'));
console.log(artGallery.showGalleryInfo('article'));
console.log(artGallery.showGalleryInfo('guest'));
// article name edge case sase sensitive!!!!