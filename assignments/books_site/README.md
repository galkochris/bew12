1. To filter for all words containing Django,
    we would .filter(title__contains = 'Django')
2. to filter for all words with the Fiction tag,
    we would .filter(tag__name = "Fiction')
3. to filter for all the authors who have written books with the word Django,
    we would Author.objects.filter(book__title__contains = 'Django')