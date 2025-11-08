# 🧠 PDC Chapter-3 – Process Management in Python

This chapter explores how Python’s **`multiprocessing`** module allows concurrent execution, inter-process communication, synchronization, and control of background processes.

---

## ⚙️ Communicating_with_pipe.py  
### **Purpose**  
To demonstrate how two or more processes communicate directly using a `Pipe` connection.  

### **Observation**  
Data was exchanged successfully between connected processes. The `Pipe` mechanism allowed duplex communication without shared memory.

---

## ⚙️ Communicating_with_queue.py  
### **Purpose**  
To illustrate how processes can exchange data safely using a `Queue`.  

### **Observation**  
The queue enabled secure message passing among multiple processes. Order of retrieval matched FIFO behavior, preventing race conditions.

---

## ⚙️ Killing_processes.py  
### **Purpose**  
To show how a running process can be terminated and joined safely.  

### **Observation**  
The target process was stopped before completion and properly cleaned up using `terminate()` and `join()`, confirming reliable process lifecycle control.

---

## ⚙️ myFunc.py  
### **Purpose**  
Contains a reusable function used by multiple multiprocessing scripts to simulate CPU-bound work.  

### **Observation**  
Acts as a helper module providing computation logic. All other scripts imported and executed it successfully within separate processes.

---

## ⚙️ naming_processes.py  
### **Purpose**  
To demonstrate assigning explicit names to processes for easier tracking and debugging.  

### **Observation**  
Each process displayed its unique name during execution, improving clarity and monitoring of concurrent tasks.

---

## ⚙️ process_in_subclass.py  
### **Purpose**  
To show how to create custom process classes by subclassing `multiprocessing.Process`.  

### **Observation**  
Subclassing provided greater control over initialization and execution steps, allowing encapsulated behavior within process objects.

---

## ⚙️ process_pool.py  
### **Purpose**  
To demonstrate parallel execution using a process pool for distributing tasks automatically.  

### **Observation**  
Workload was efficiently shared among multiple worker processes, significantly reducing total computation time.

---

## ⚙️ processes_barrier.py  
### **Purpose**  
To demonstrate synchronization among processes using `Barrier` and `Lock`.  

### **Observation**  
All processes waited for one another at the barrier before proceeding, ensuring synchronized and orderly execution.

---

## ⚙️ run_background_processes.py  
### **Purpose**  
To demonstrate running background tasks concurrently with the main process.  

### **Observation**  
Background processes executed independently while the main program continued, confirming proper concurrent behavior.

---

## ⚙️ run_background_processes_no_daemon.py  
### **Purpose**  
To compare daemon and non-daemon background processes.  

### **Observation**  
Daemon processes ended automatically when the main process exited, while non-daemon processes completed normally, highlighting lifecycle differences.

---

## ⚙️ Spawning_processes.py  
### **Purpose**  
To demonstrate dynamically creating and launching multiple processes in a loop.  

### **Observation**  
Multiple processes were spawned and executed independently. Each process handled its own workload, confirming effective parallel execution.

---

## 🧩 Summary

| Script Name | Purpose Summary | Observation Summary |
| :----------------------------------- | :------------------------------------------- | :---------------------------------------------------------- |
| Communicating_with_pipe.py | Inter-process communication using `Pipe` | Data exchange succeeded through direct duplex connection |
| Communicating_with_queue.py | Communication using `Queue` | Safe and ordered message passing achieved |
| Killing_processes.py | Process termination control | Processes terminated and joined cleanly |
| myFunc.py | Shared computation function | Provided CPU-bound work logic for other scripts |
| naming_processes.py | Assigning process names | Clear identification of concurrent processes |
| process_in_subclass.py | Subclassing Process class | Custom process behavior successfully implemented |
| process_pool.py | Using process pools for parallel work | Work efficiently distributed among worker processes |
| processes_barrier.py | Synchronization via Barrier & Lock | Ordered execution ensured through synchronization |
| run_background_processes.py | Running background tasks | Independent background execution verified |
| run_background_processes_no_daemon.py | Daemon vs Non-Daemon comparison | Lifecycle difference observed between process types |
| Spawning_processes.py | Spawning processes dynamically | Independent and scalable process execution confirmed |

---

## 🧠 Overall Learning

This chapter provides a hands-on understanding of **process creation, communication, synchronization, and management** using Python’s `multiprocessing` module.  
Each example reinforces practical concepts of concurrency, helping build reliable and efficient parallel applications.
