### Learnings

Multi Tier Architectures

Three-tier architecture is a well-established software application architecture that organizes applications into three logical and physical computing tiers: 

* the presentation tier, or user interface

  - HTML, CSS, JS generally for web, for applications the language can be platform specific

  - provides GUI and can interact with the application tier using API calls

* the application tier, where data is processed

  - Python, Java, PHP, Ruby, Perl
  - can add, modify and delete data in the data tier
  - communicates with the data tier using API calls

* and the data tier, where the data associated with the application is stored and managed

  - SQL Database Servers - PostgreSQL, MySQL, MariaDB, Oracle, DB2, Informix, Microsoft SQL Server
    NoSQL Database Servers - Cassandra, CouchDB or MongoDB

The chief benefit of three-tier architecture is that because each tier runs on its own infrastructure, each tier can be developed simultaneously by a separate development team, and can be updated or scaled as needed without impacting the other tiers.

### Tier vs Layer

They aren't the same.
A 'layer' refers to a functional division of the software, but a 'tier' refers to a functional division of the software that runs on infrastructure separate from the other divisions. 
The Contacts app on your phone, for example, is a *three*-*layer* application, but a *single-tier* application, because all three layers run on your phone.
The difference is important, because layers can't offer the same benefits as tiers.

### Benefits

Other benefits (compared to single- or two-tier architecture) include:

- **Faster development**: Because each tier can be developed simultaneously by different teams, an organization can bring the application to market faster, and programmers can use the latest and best languages and tools for each tier.
- **Improved scalability**: Any tier can be scaled independently of the others as needed.
- **Improved reliability**: An outage in one tier is less likely to impact the availability or performance of the other tiers.
- **Improved security**: Because the presentation tier and data tier can't communicate directly, a well-designed application tier can function as a sort of internal firewall, preventing SQL injections and other malicious exploits.

## Docker

Docker is open-source technology—and a container file format—for automating the deployment of applications as portable, self-sufficient containers that can run in the cloud or on-premises. 

Docker features the Docker Engine, which is a runtime environment. It allows you to build and run containers on any development machine; then store or share container images through a container registry like Docker Hub or Azure Container Registry.



## Kubernetes

Kubernetes is open-source orchestration software that provides an API to control how and where those containers will run. It allows you to run your Docker containers and workloads and helps you to tackle some of the operating complexities when moving to scale multiple containers, deployed across multiple servers.



---

A fundamental difference between Kubernetes and Docker is that Kubernetes is meant to run across a cluster while Docker runs on a single node. 

---

## YAML

* Yet another markup language / YAML ain't markup language
* Serialisation language - *Serialization* or *marshaling* is the process of converting object state into a format that can be transmitted or stored. The serialization changes the object state into series of bits. The object state could be reconstructed later in the opposite process, called *deserialization* or *unmarshalling*. The reconstructed object is a semantically identical clone to the original object. The object after serialization is called *archive*. Serialization is a low-level technique that violates encapsulation and breaks the opacity of an abstract data type.
* The file starts with three dashes. These dashes indicate the start of a new YAML document.
* Indentation is how YAML denotes nesting. The number of spaces can vary from file to file, but tabs are not allowed. 

```yaml
---
 doe: "a deer, a female deer"
 ray: "a drop of golden sun"
 pi: 3.14159
 xmas: true
 french-hens: 3
 calling-birds:
   - huey
   - dewey
   - louie
   - fred
 xmas-fifth-day:
   calling-birds: four
   french-hens: 3
   golden-rings: 5
   partridges:
     count: 1
     location: "a pear tree"
   turtle-doves: two
```

* yaml can have multiple data types like int, float, strings, arrays, booleans.
* Below is how a yaml file is when it is converted in json format

```json
{
  "doe": "a deer, a female deer",
  "ray": "a drop of golden sun",
  "pi": 3.14159,
  "xmas": true,
  "french-hens": 3,
  "calling-birds": [
     "huey",
     "dewey",
     "louie",
     "fred"
  ],
  "xmas-fifth-day": {
  "calling-birds": "four",
  "french-hens": 3,
  "golden-rings": 5,
  "partridges": {
    "count": 1,
    "location": "a pear tree"
  },
  "turtle-doves": "two"
  }
}
```

* Comments in yaml use a # symbol

```yaml
___
# This is a full line comment
foo: bar # this is a comment, too
```

* We can also represent Not-A-Number Nan or infinity

```yaml
---
foo: .inf
bar: -.Inf
plop: .NAN
```

**Foo** is infinity. **Bar** is negative infinity, and **plop** is NAN.

---

## Ray

Ray provides a simple, universal API for building distributed applications.

Ray accomplishes this mission by:

1. Providing simple primitives for building and running distributed applications.
2. Enabling end users to parallelize single machine code, with little to zero code changes.
3. Including a large ecosystem of applications, libraries, and tools on top of the core Ray to enable complex applications.

**Ray Core** provides the simple primitives for application building.

On top of **Ray Core** are several libraries for solving problems in machine learning:

- [Tune: Scalable Hyperparameter Tuning](https://docs.ray.io/en/master/tune/index.html)
- [RLlib: Scalable Reinforcement Learning](https://docs.ray.io/en/master/rllib.html#rllib-index)
- [RaySGD: Distributed Training Wrappers](https://docs.ray.io/en/master/raysgd/raysgd.html#sgd-index)
- [Ray Serve: Scalable and Programmable Serving](https://docs.ray.io/en/master/serve/index.html#rayserve)

---

## SQLITE

#### Advantages of SQLite

- File based:
  The entire database consists of a single file on the disk, which makes it extremely portable.

- Standards-aware:
  Although it might appear like a “simple” DB implementation, SQLite uses SQL. It has some features omitted (`RIGHT OUTER JOIN` or `FOR EACH STATEMENT`), however, some additional ones are baked in.

- Great for developing and even testing:
  During the development phase of most applications, for a majority of people it is extremely likely to need a solution that can scale for concurrency. SQLite, with its rich feature base, can offer more than what is needed for development with the simplicity of working with a single file and a linked C based library.

#### Disadvantages of SQLite

- No user management:
  Advanced databases come with the support for users, i.e. managed connections with set access privileges to the database and tables. Given the purpose and nature of SQLite (no higher-levels of multi-client concurrency), this feature does not exist.

- Lack of possibility to tinker with for additional performance:
  Again by design, SQLite is not possible to tinker with to obtain a great deal of additional performance. The library is simple to tune and simple to use. Since it is not complicated, it is technically not possible to make it more performant than it already, amazingly is.

#### When To Use SQLite

- Embedded applications:
  All applications that need portability, that do not require expansion, e.g. single-user local applications, mobile applications or games.

- Disk access replacement:
  In many cases, applications that need to read/write files to disk directly can benefit from switching to SQLite for additional functionality and simplicity that comes from using the *Structured Query Language*(SQL).

- Testing:
  It is an overkill for a large portion of applications to use an additional process for testing the business-logic (i.e. the application’s main purpose: functionality).

#### When Not To Use SQLite

- Multi-user applications:
  If you are working on an application whereby multiple clients need to access and use the same database, a fully-featured RDBM (e.g. MySQL) is probably better to choose over SQLite.

- Applications requiring high write volumes:
  One of the limitations of SQLite is the *write* operations. This DBMS allows only one single write*operating to take place at any given time, hence allowing a limited throughput.

---

## MySQL

#### Advantages of MySQL

- Easy to work with:
  MySQL can be installed very easily. Third-party tools, including visual ones (i.e. GUIs) make it extremely simple to get started with the database.

- Feature rich:
  MySQL supports a lot of the SQL functionality that is expected from a RDBMS — either directly or indirectly.

- Secure:
  A lot of security features, some rather advanced, are built in MySQL.

- Scalable and powerful:
  MySQL can handle *a lot* of data and furthermore it can be used “at scale”, if needed be.

- Speedy:
  Giving up some standards allows MySQL to work very efficiently and cut corners, thus providing speed gains.

#### Disadvantages of MySQL

- Known limitations:
  By design, MySQL does not intend to do everything and it comes with functional limitations that some state-of-the-art applications might require.

- Reliability issues:
  The way certain functionality gets handled with MySQL (e.g. references, transactions, auditing etc.) renders it a little-less reliable compared to some other RDBMSs.

- Stagnated development:
  Although MySQL is still technical an open-source product, there are complaints regarding the development process since its acquisition. However, it should be noted that there are some MySQL-based, fully-integrated databases that add value on top of the standard MySQL installations (e.g. MariaDB).

#### When To Use MySQL

- Distributed operations:
  When you need more than what SQLite can offer, including MySQL to your deployment stack, just like any stand-alone database server, brings a lot of operational freedom together with some advanced features.

- High security:
  MySQL’s security features provide reliable protection for data-access (and use) in a simple way.

- Web-sites and web-applications:
  A great majority of web-sites (and web-applications) can simply work on MySQL despite the constraints. This flexible and somewhat scalable tool is easy to use and easy to manage — which proves very helpful in the long run.

- Custom solutions:
  If you are working on a highly specific and extremely custom solution, MySQL can tag along easily and go by your rules thanks to its rich configuration settings and operation modes.

#### When Not To Use MySQL

- SQL compliance:
  Since MySQL does not [try to] implement the full SQL standard, this tool is not completely SQL compliant. If you might need integration with such RDBMSs, switching from MySQL will not be easy.

- Concurrency:
  Even though MySQL and some storage engines perform really well with *read* operations, concurrent *read-writes* can be problematic.

- Lack of features:
  Again, depending on the choice of the database-engine, MySQL can lack certain features, such as the full-text search.

---

## PostgreSQL

#### Advantages of PostgreSQL

- An open-source SQL standard compliant RDBMS:
  PostgreSQL is open-source and free, yet a very powerful relational database management system.

- Strong community:
  PostgreSQL is supported by a devoted and experienced community which can be accessed through knowledge-bases and Q&A sites 24/7 for free.

- Strong third-party support:
  Regardless of the extremely advanced features, PostgreSQL is adorned with many great and open-source third-party tools for designing, managing and using the management system.

- Extensible:
  It is possible to extend PostgreSQL programmatically with stored procedures, like an advanced RDBMS should be.

- Objective:
  PostgreSQL is not just a relational database management system but an objective one — with support for nesting, and more.

#### Disadvantages of PostgreSQL

- Performance:
  For simple *read*-heavy operations, PostgreSQL can be an over-kill and might appear less performant than the counterparts, such as MySQL.

- Popularity:
  Given the nature of this tool, it lacks behind in terms of popularity, despite the very large amount of deployments — which might affect how easy it might be possible to get support.

- Hosting:
  Due to above mentioned factors, it is harder to come by hosts or service providers that offer managed PostgreSQL instances.

#### When To Use PostgreSQL

- Data integrity:
  When reliability and data integrity are an absolute necessity without excuses, PostgreSQL is the better choice.

- Complex, custom procedures:
  If you require your database to perform custom procedures, PostgreSQL, being extensible, is the better choice.

- Integration:
  In the future, if there is a chance of necessity arising for migrating the entire database system to a propriety (e.g. Oracle) solution, PostgreSQL will be the most compliant and easy to handle base for the switch.

- Complex designs:
  Compared to other open-source and free RDBMS implementations, for complex database designs, PostgreSQL offers the most in terms of functionality and possibilities without giving up on other valuable assets.

#### When Not To Use PostgreSQL

- Speed:
  If all you require is fast *read* operations, PostgreSQL is not the tool to go for.

- Simple set ups:
  Unless you require absolute data integrity, ACID compliance or complex designs, PostgreSQL can be an over-kill for simple set-ups.

- Replication:
  Unless you are willing to spend the time, energy and resources, achieving replication with MySQL might be simpler for those who lack the database and system administration experience.

  ![DB Comparison Table]('./dbcomparison.png')


