const {expect} = require('chai');
const rgbToHexColor = require('../RGBToHex');

describe('Test RGB to Hex Color Functionality', () => {
    let numArg = 1;
    let stringArg = '1';
    let failureResult = undefined;
    let result = '#010101';

    it('Test if one argument is string', () => {
        expect(rgbToHexColor(numArg, numArg, stringArg)).to.be.undefined;
    });

    it('Test if one argument is Over 255', () => {
        expect(rgbToHexColor(numArg, 256, numArg)).to.be.undefined;
        expect(rgbToHexColor(256, numArg, numArg)).to.be.undefined;
        expect(rgbToHexColor(numArg, numArg, 256)).to.be.undefined;
        expect(rgbToHexColor(256, 256, 256)).to.be.undefined;
    });

    it('Test if one argument negative number', () => {
        expect(rgbToHexColor(-10, numArg, numArg)).to.be.undefined;
    });

    it('Test if correct input give expected result', () => {
        expect(rgbToHexColor(numArg, numArg, numArg)).to.equal(result);
        expect(rgbToHexColor(255, 255, 255)).to.equal('#FFFFFF');
        expect(rgbToHexColor(0, 0, 0)).to.equal('#000000');
        expect(rgbToHexColor(0, 255, 0)).to.equal('#00FF00');
        expect(rgbToHexColor(0, 0, 255)).to.equal('#0000FF');
    });

    it('Test for missing parameters', () => {
        expect(rgbToHexColor(255)).to.be.undefined;
        expect(rgbToHexColor(255, 255)).to.be.undefined;
    });

});