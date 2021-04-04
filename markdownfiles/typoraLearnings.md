# Typora Learnings

_italics_ - Words that begin and end with an underscore _ are italisized

**bold** - Words that are in between a double ** asterisk are made bold.

_**both bold and italiscs**_ - can be done by using an underscore _ and double asterisk together **

Headers in Markdown - can be done by putting the correct number of # hashtags in front of headers 

# Header one 

## Header two

### Header three

#### Header four
##### Header five
###### Header six



### Links in Markdown

There are two different link types in Markdown, but both of them render the exact same way. The first link style is called an *inline link*. To create an inline link, you wrap the link text in brackets ( `[ ]` ), and then you wrap the link in parenthesis ( `( )` ). For example, to create a hyperlink to www.github.com, with a link text that says, Visit GitHub!, you'd write this in Markdown: `[Visit GitHub!](www.github.com)`.

[This link goes to google](www.google.com)

The other link type is called a *reference* link. As the name implies, the link is actually a reference to another place in the document.

Do you want to [see something fun][a fun place]?

Well, do I have [the website for you][another fun place]!
[a fun place]: www.zombo.com
[another fun place]: www.stumbleupon.com

Images also have two styles, just like links, and both of them render the exact same way. The difference between links and images is that images are prefaced with an exclamation point ( `!` ).

The first image style is called an *inline image link*. To create an inline image link, enter an exclamation point ( `!` ), wrap the alt text in brackets ( `[ ]` ), and then wrap the link in parenthesis ( `( )` ).

![A pretty tiger](https://upload.wikimedia.org/wikipedia/commons/5/56/Tiger.50.jpg)

For a reference image, you'll follow the same pattern as a reference link. You'll precede the Markdown with an exclamation point, then provide two brackets for the alt text, and then two more for the image tag, like this: `![The founding father][Father]`

![Black cat][Black]

![Orange cat][Orange]

[Black]: https://upload.wikimedia.org/wikipedia/commons/a/a3/81_INF_DIV_SSI.jpg
[Orange]:http://icons.iconarchive.com/icons/google/noto-emoji-animals-nature/256/22221-cat-icon.png

#BlockQuotes

I read this interesting quote the other day:

>"Her eyes had called him and his soul had leaped at the call. To live, to err, to fall, to triumph, to recreate life out of life!"

To group them together each line that is empty must also have the carrot > symbol

>Once upon a time and a very good time it was there was a moocow coming down along the road and this moocow that was coming down along the road met a nicens little boy named baby tuckoo...
>
>His father told him that story: his father looked at him through a glass: he had a hairy face.
>
>He was baby tuckoo. The moocow came down the road where Betty Byrne lived: she sold lemon platt.

# Lists

* Flour
* Cheese
* Tomatoes

1. Cut the cheese
2. Slice the tomatoes
3. Rub the tomatoes in flour

Leave space before the second asterisk so that the second point is nested under the first point

* Calculus 
* A professor
 * Has no hair
 * Often wears green
* Castafiore
 * An opera singer
 * Has white hair
 * Is possibly mentally unwell

To make a soft break that is to close the distance between the next lines leave 2 spaces after each line

We pictured the meek mild creatures where  
They dwelt in their strawy pen,  
Nor did it occur to one of us there  
To doubt they were kneeling then.

Strikethrough Using double ~~ tildes ~~

~~Like This~~

# Inline Code

`Backtick for inline code`

```This is a multiple line code segment
Yes it looks like this
#include<iostream.h>
#inlude<conio.h>
int main()
{
	clrscr();
	int blahblahblah;
	printf("Hello Markdown");
	getch();
}
```

Horizontal line can be made using 3 hyphenns - or 3 asterisks or 3 underscores

---

Task Lists

- [] can be created like this
  - [x] done list
  - [ ] empty
  - [ ] empty
  - [ ] completed task
  - [ ] - [x]

#### Emoji 

:+1: Thumbs up emoji +1

:a: 

