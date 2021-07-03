### Things to remember while using ray - 

1. `ray start --head --redis-port=8888` should be used on the main computer which will start the process. 

2. On other computers we have to start its own client node and so other computers have to be in the same network (either via LAN or WiFi or some cloud service) and they must run the `ray start --address='192.168.0.39:8888' --redis-password='5241590000000000'`command in the command line. 
   
3. To connect a driver to the cluster from Python we add the following to the file -

   ```python
   import ray
   ray.init(address='192.168.0.38:8888', redis-password='5241590000000000')
   ```

4. All the computers must have the same version of ray and same version of python. (Basically the same dependencies on all the systems or else we'll get an error)
   
5. Can use `htop` to see system usage stats. Also can see the stats from ray dashboard
   
6. In the dashboard, the logical view can show the stats, print statement results, errors, etc.
   
7. `@ray.remote` decorator has to be given for functions that we want to execute parallely

8. other functions can be called directly

9. Have to see how to use `ray.get(object_name)` works, because a remote function returns a future, which is basically an object id.
   
10. Have to see how to extract methods/functions if they are passed/returned.
    
11. Have to see what happens in case of a server error. (If everything is proper and the data leads to an error then how to recover that node)


---

### Using Ray

`pip install ray[serve]`

Parallelizing functions - Add the following decorator `@ray.remote` above the function we want to parallelize. Call the function with `.remote()` instead of calling it normally. This remote call yields a future, or `ObjectRef` that you can then fetch with `ray.get`

```python
import ray
ray.init()

@ray.remote
def f(x):
	return x*x
	
futures=[f.remote(i) for i in range(4)]
print(ray.get(futures))
```

Parallelizing classes - Ray provides actors to allow you to parallelize an instance of a class in Python/Java. When you instantiate a class that is a Ray actor, Ray will start a remote instance of that class in the cluster. This actor can then execute remote method calls and maintain its own internal state.

```python
import ray
ray.init()

@ray.remote
class Counter(object):
	def __init__(self):
		self.n=0
	def increment(self):
		self.n+=1
	def read(self):
		return self.n
		
counters=[Counter.remote() for i in range(4)]
[c.increment.remote() for c in counters]
futures=[c.read.remote() for c in counters]
print(ray.get(futures))
```

Terminating Actors:

```python
ray.actor.exit_actor()
```

or

```
ray.kill(actor_handle)
```

## Passing Around Actor Handles[¶](https://docs.ray.io/en/master/actors.html#passing-around-actor-handles)

Actor handles can be passed into other tasks. We can define remote functions (or actor methods) that use actor handles.

```python
import time

@ray.remote
def f(counter):
    for _ in range(1000):
        time.sleep(0.1)
        counter.increment.remote()
```

If we instantiate an actor, we can pass the handle around to various tasks.

```python
counter = Counter.remote()

# Start some tasks that use the actor.
[f.remote(counter) for _ in range(3)]

# Print the counter value.
for _ in range(10):
    time.sleep(1)
    print(ray.get(counter.get_counter.remote()))
```

---

Actor Pool

The `ray.util` module contains a utility class, `ActorPool`. This class is similar to multiprocessing.Pool and lets you schedule Ray tasks over a fixed pool of actors.

```python
from ray.util import ActorPool

a1, a2 = Actor.remote(), Actor.remote()
pool = ActorPool([a1, a2])
print(pool.map(lambda a, v: a.double.remote(v), [1, 2, 3, 4]))
# [2, 4, 6, 8]

```

* This code snippet above can be used in our code when we want to call functions that are in a class that is defined with a `@ray.remote()` decorator

---

Custom Response - HTML, Stream, File, others

response_class=HTMLResponse

response_class=
