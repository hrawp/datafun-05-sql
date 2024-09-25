SELECT authors.author_id, authors.first, authors.last, books.title
FROM authors 
INNER JOIN books ON authors.author_id = books.author_id;