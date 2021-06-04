# Ray Learnings

RayServe is a scalable model-serving library built on Ray.

`pip3 install -U ray` to install ray

To start ray add `ray.init()` to the python file

 ```python
 import ray
 ray.init()	#To initialise ray in the python file
 ```

Difference between regular functions in python and remote function which are called asynchronous functions in ray.

```python
# A regular Python function.
def regular_function():
    return 1

# A Ray remote function.
@ray.remote
def remote_function():
    return 1
```

1. **Invocation:** The regular version is called with `regular_function()`, whereas the remote version is called with `remote_function.remote()`.
2. **Return values:** `regular_function` immediately executes and returns `1`, whereas `remote_function` immediately returns an object ID (a future) and then creates a task that will be executed on a worker process. The result can be retrieved with `ray.get`.
3. **Parallelism:** Invocations of `regular_function` happen **serially**, whereas invocations of `remote_function` happen in **parallel**.

```python
assert regular_function() == 1

object_id = remote_function.remote()

# The value of the original `regular_function`
assert ray.get(object_id) == 1
```

```python
# These happen serially.
for _ in range(4):
    regular_function()
    
# These happen in parallel.
for _ in range(4):
    remote_function.remote()
```

**Object IDs** can also be passed into remote functions. When the function actually gets executed, **the argument will be a retrieved as a regular Python object**. 

```python
@ray.remote
def remote_chain_function(value):
    return value + 1


y1_id = remote_function.remote()
assert ray.get(y1_id) == 1

chained_id = remote_chain_function.remote(y1_id)
assert ray.get(chained_id) == 2
```

The `ray.init()` command will automatically detect the available GPUs and CPUs on the machine. However, you can override this default behavior by passing in specific resources, e.g., `ray.init(num_cpus=8, num_gpus=4, resources={'Custom': 2})`. Default is 1 CPU.

