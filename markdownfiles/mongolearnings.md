# MongoDB Learnings

* Scales Horizontally
* Is Simple and Fast
* No need to structure the database
* everything can be added as a document, data, records, row, json. 

## MongoDB Shell

* `db` - db refers to the current database and typing this prints it. test is the output by default which is the default database.
* `use <db>` - to switch to a different database. Ex: `use examples`
* all objects that we insert in mongodb have by default a `_id` field that holds the object ID and is unique.
* `show dbs` - to show the list of all databases
* `show collections` - to show the collections present in the current db
* `db.dropDatabase()` - to drop the current database i.e., to delete it
* `use mynewdb` - to create a new database named mynewdb, but if we run `show dbs` after this command then it won't show `mynewdb` because it doesn't have any data in it, i.e, it is empty so it doesn't show up.
* `db.createCollection('posts')` - to create a collection in our current db names `posts`
* `{'ok':1}` - we get after inserting or creating, etc to denote successful operation.

```json
db.posts.insert({
	title:'Post One',
	body: 'Body of post one',
	category: 'News',
    likes: 4,
    tags: ['news','events'],
    user: {
        name: 'John Doe',
        status: 'author'
    },
	date: Date()
})
```

* The above line inserts a json record as defined into the collection - `posts` of the current db. Will show `WriteResult({"nInserted":1})` which means successfully inserted.

```json
db.posts.insertMany([
	{
		title: 'Post Two',
		body: 'Body of post two',
		category: 'Technology',
		date: Date()
	},
	{
		title: 'Post Three',
		body: 'Body of post three',
		category: 'News',
		date: Date()
	},
	{
		title: 'Post Four',
		body: 'Body of post four',
		category: 'Entertainment',
		date: Date()
	}
])
```

* After inserting the above 3 objects I got a result like this 

  ```json
  {
  	"acknowledged" : true,
  	"insertedIds" : [
  		ObjectId("60b8bdf9ac39a6c9af0e6292"),
  		ObjectId("60b8bdf9ac39a6c9af0e6293"),
  		ObjectId("60b8bdf9ac39a6c9af0e6294")
  	]
  }
  ```

---

### Now to query the data

* `db.posts.find()` - to query all the elements in the current database in the collection find.
* `db.posts.find().pretty()` - to make it display the output properly so that it is easier to read.
* `db.posts.find({ category: 'News' })` - to display the objects/items which have the category as 'News'. This is similar to the `WHERE` clause in SQL.
* `db.posts.find( category : 'News' ).pretty()` - to display the above query but in a more pretty or readable format.
* `db.posts.find().sort({ title: 1}).pretty()` - to sort the elements/rows/items according to title in ascending order. 1 is for ascending order and -1 is for descending order.
* `db.posts.find().sort({ title: -1 }).pretty()` - to sort in descending order. -1 is for descending.
* `db.posts.find({category: 'News' }).count()` - to count the number of elements. In this case we are finding the elements which have `category` as `news` and `count()` is used to count the elements/rows/objects returned which in this case is 2.
* `db.posts.find().limit(2)` - to limit the entries show to the number we want. In this case we are limiting to just 2.
* `db.posts.find().sort({title:-1}).limit(2).pretty()` - Here we are finding all the entries from the collection `posts` in the current db and the we are sorting it in descending order and limiting to only 2 posts and then finally making it pretty. Thus we can chain functions here.

---

## Other queries that can be done

* `db.posts.find().forEach(function(doc){ print('Blog Post: '+ doc.title)})` - this is the forEach function which can loop over multiple entries and takes in a function. Output obtained was as below:

  ```json
  > db.posts.find().forEach(function(doc){ print('Blog Post: '+ doc.title)})
  Blog Post: Post One
  Blog Post: Post Two
  Blog Post: Post Three
  Blog Post: Post Four
  ```

* `db.posts.findOne({category: 'News'})` - this function will only display the first entry from the collection posts where the category is `News`

---

### Updating in DB

* ```json
  db.posts.update({ title: 'Post Two'},
  {
  	title: 'Post Two',
  	body: 'New post 2 body',
  	date: Date()
  },
  {
  	upsert: true
  })
  ```

  Here, upsert check if the item is found or not, if it is not found then it will create an element with the fields entered.

* ```json
  db.posts.update({ title: 'Post Two' },
  {
  	$set: {
  		body: 'Body of post 2',
  		category: 'Technology'
  	}
  })
  ```

  Here the `$set` operator will change on the fields that we've mentioned but will not affect the existing data.

* Increment operator to increment some value in the collections field

  ```json
  db.posts.update({ title: 'Post One' }, { $inc: { likes: 2}})
  ```

* Rename fields

  ```json
  db.posts.update({ title: 'Post One'}, {$rename: { likes: 'views'}})
  ```

---

### Deleting in DB

* ```json
  db.posts.remove({ title: 'Post Four' })
  ```

  To remove an element from the db collection. Normally it is better to use ObjectID because it is unique.

* ```json
  db.posts.update({title:'Post One'},
  {
  	$set: {
  		comments: [
  			{
  				user: 'Mary Williams',
  				body: 'Comment One',
  				date: Date()
  			},
  			{
  				user: 'Harry White',
  				body: 'Comment Two',
  				date: Date()
  			}
  		]
  	}
  })
  ```

  Here we showed that if we want to add extra comments then we can do that easily.

*  ```json
   db.posts.find({
   	comments: {
   		$elemMatch: {
   			user: 'Mary Williams'
   		}
   	}
   })
   ```

  Here we are finding all the posts that have the comment by `Mary Williams` we can do this by using the `$elemMatch` operator.

* Now to do text search, we can add indexes, using the `createIndex() operator.`

  ```json
  db.posts.createIndex({title:'text'})
  ```

  Now we can use the follwing:

  ```json
  db.posts.find({
  	$text: {
  		$search: "\"Post O\""
  	}
  })
  ```

  The above code searched for the text that starts from `Post O` in the collection like `Post One` and return that.

  ```json
  db.posts.find({
  	$text: {
  		$search: "\"Post T\""
  	}
  })
  ```

  The above code searched for the text that starts from `Post T` in the collection and will return what it finds. Here it found `Post Two` and `Post Three`

* ```json
  db.posts.update({ title: 'Post Two'},{ $set: { views:10}})
  ```

  ```json
  db.posts.find({ views: { $gt: 3}})
  ```

  Here we were updating one of the posts with views equal to 10 and then checking the find operator with views that are greater than 3. `$gt` operator is for greater than.

  We can also do greater than or equal to using `$gte`. Less than or equal to using `$lte` and less than using `$lt` operator.

  ```json
  db.posts.find({views: { $gte:6}})
  ```

* `exit` to exit the shell.

---

### Deleting

* To drop a database we switch to that database using `use dbname` and then we use the following:

  ```json
  db.dropDatabase()
  ```

* To drop a collection we switch to the desired database using `use dbname` and then we write the collection name in place of the `collection` word by typing the following:

  ```json
  db.collection.drop()
  ```

* To delete documents from a collection we can use `deleteOne` or `deleteMany` like:

  ```json
  db.movies.deleteOne({cast:"ActorName"})
  db.movies.deleteMany({views:5})
  ```

---

## Pymongo

This is the python mongodb library. It allows interaction of the MongoDB database using Python.



