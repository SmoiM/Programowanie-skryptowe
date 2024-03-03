'use strict'

var expect = chai.expect;

function sum(x,y) {
	return x+y;
}

describe('The sum() function', function() {
    
    it('Returns 4 for 2 + 2', function() {
        expect(sum(2, 2)).to.equal(4);
    });
    it('Returns 0 for -2 + 2', function() {
        expect(sum(-2, 2)).to.equal(0);
    });
});

describe('Testy', function() {
    it("cyfry", function() {
        chai.assert.equal(cyfry('123'), 6);
		chai.assert.equal(cyfry('aa'), 0);
		chai.assert.equal(cyfry('aa12'), 3);
		chai.assert.equal(cyfry('12aa'), 3);
		chai.assert.equal(cyfry(''), 0);
    });
	
    it("litery", function() {
        chai.assert.equal(litery('123'), 0);
		chai.assert.equal(litery('aa'), 2);
		chai.assert.equal(litery('aa00'), 2);
		chai.assert.equal(litery('00aa'), 2);
		chai.assert.equal(litery(''), 0);
    })
	
    it("suma", function() {
		total = 0;
        chai.assert.equal(suma('123'), 123);
		chai.assert.equal(suma('hg'), 123);
		chai.assert.equal(suma('cr11'), 123);
		chai.assert.equal(suma('11qwe'), 134);
		chai.assert.equal(suma(''), 134);
    })
});
