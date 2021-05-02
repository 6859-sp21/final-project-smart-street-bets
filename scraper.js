import cheerio from 'cheerio';
import fetch from 'node-fetch';


const keyword = 'Bitcoin';
const econ = 'https://economist.com';

function getArticles(resp) {
    fetch(econ)
    .then(res => res.text())
    .then(html => resp(html));
}