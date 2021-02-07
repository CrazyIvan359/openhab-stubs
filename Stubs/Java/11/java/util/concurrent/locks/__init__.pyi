import java.io
import java.lang
import java.util
import java.util.concurrent
import typing


class AbstractOwnableSynchronizer(java.io.Serializable):
    """
    Java class 'java.util.concurrent.locks.AbstractOwnableSynchronizer'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
    """

class Condition(java.lang.Object):
    """
    public interface Condition
    
        :code:`Condition` factors out the :code:`Object` monitor methods (:meth:`~java.lang.Object.wait`,
        :meth:`~java.lang.Object.notify` and :meth:`~java.lang.Object.notifyAll`) into distinct objects to give the effect of
        having multiple wait-sets per object, by combining them with the use of arbitrary
        :class:`~java.util.concurrent.locks.Lock` implementations. Where a :code:`Lock` replaces the use of :code:`synchronized`
        methods and statements, a :code:`Condition` replaces the use of the Object monitor methods.
    
        Conditions (also known as *condition queues* or *condition variables*) provide a means for one thread to suspend
        execution (to "wait") until notified by another thread that some state condition may now be true. Because access to this
        shared state information occurs in different threads, it must be protected, so a lock of some form is associated with
        the condition. The key property that waiting for a condition provides is that it *atomically* releases the associated
        lock and suspends the current thread, just like :code:`Object.wait`.
    
        A :code:`Condition` instance is intrinsically bound to a lock. To obtain a :code:`Condition` instance for a particular
        :class:`~java.util.concurrent.locks.Lock` instance use its :meth:`~java.util.concurrent.locks.Lock.newCondition` method.
    
        As an example, suppose we have a bounded buffer which supports :code:`put` and :code:`take` methods. If a :code:`take`
        is attempted on an empty buffer, then the thread will block until an item becomes available; if a :code:`put` is
        attempted on a full buffer, then the thread will block until a space becomes available. We would like to keep waiting
        :code:`put` threads and :code:`take` threads in separate wait-sets so that we can use the optimization of only notifying
        a single thread at a time when items or spaces become available in the buffer. This can be achieved using two
        :class:`~java.util.concurrent.locks.Condition` instances.
    
        .. code-block: java
        
         class BoundedBuffer<E> {
           **final Lock lock = new ReentrantLock();**
           final Condition notFull  = **lock.newCondition();**
           final Condition notEmpty = **lock.newCondition();**
        
           final Object[] items = new Object[100];
           int putptr, takeptr, count;
        
           public void put(E x) throws InterruptedException {
             **lock.lock();
             try {**
               while (count == items.length)
                 **notFull.await();**
               items[putptr] = x;
               if (++putptr == items.length) putptr = 0;
               ++count;
               **notEmpty.signal();**
             **} finally {
               lock.unlock();
             }**
           }
        
           public E take() throws InterruptedException {
             **lock.lock();
             try {**
               while (count == 0)
                 **notEmpty.await();**
               E x = (E) items[takeptr];
               if (++takeptr == items.length) takeptr = 0;
               --count;
               **notFull.signal();**
               return x;
             **} finally {
               lock.unlock();
             }**
           }
         }
         
        (The :class:`~java.util.concurrent.ArrayBlockingQueue` class provides this functionality, so there is no reason to
        implement this sample usage class.)
    
        A :code:`Condition` implementation can provide behavior and semantics that is different from that of the :code:`Object`
        monitor methods, such as guaranteed ordering for notifications, or not requiring a lock to be held when performing
        notifications. If an implementation provides such specialized semantics then the implementation must document those
        semantics.
    
        Note that :code:`Condition` instances are just normal objects and can themselves be used as the target in a
        :code:`synchronized` statement, and can have their own monitor :meth:`~java.lang.Object.wait` and
        :meth:`~java.lang.Object.notify` methods invoked. Acquiring the monitor lock of a :code:`Condition` instance, or using
        its monitor methods, has no specified relationship with acquiring the :class:`~java.util.concurrent.locks.Lock`
        associated with that :code:`Condition` or the use of its :meth:`~java.util.concurrent.locks.Condition.await` and
        :meth:`~java.util.concurrent.locks.Condition.signal` methods. It is recommended that to avoid confusion you never use
        :code:`Condition` instances in this way, except perhaps within their own implementation.
    
        Except where noted, passing a :code:`null` value for any parameter will result in a
        :class:`~java.lang.NullPointerException` being thrown.
    
        Implementation Considerations
    -----------------------------
    
    
        When waiting upon a :code:`Condition`, a "*spurious wakeup*" is permitted to occur, in general, as a concession to the
        underlying platform semantics. This has little practical impact on most application programs as a :code:`Condition`
        should always be waited upon in a loop, testing the state predicate that is being waited for. An implementation is free
        to remove the possibility of spurious wakeups but it is recommended that applications programmers always assume that
        they can occur and so always wait in a loop.
    
        The three forms of condition waiting (interruptible, non-interruptible, and timed) may differ in their ease of
        implementation on some platforms and in their performance characteristics. In particular, it may be difficult to provide
        these features and maintain specific semantics such as ordering guarantees. Further, the ability to interrupt the actual
        suspension of the thread may not always be feasible to implement on all platforms.
    
        Consequently, an implementation is not required to define exactly the same guarantees or semantics for all three forms
        of waiting, nor is it required to support interruption of the actual suspension of the thread.
    
        An implementation is required to clearly document the semantics and guarantees provided by each of the waiting methods,
        and when an implementation does support interruption of thread suspension then it must obey the interruption semantics
        as defined in this interface.
    
        As interruption generally implies cancellation, and checks for interruption are often infrequent, an implementation can
        favor responding to an interrupt over normal method return. This is true even if it can be shown that the interrupt
        occurred after another action that may have unblocked the thread. An implementation should document this behavior.
    
        Since:
            1.5
    
    
    """
    def awaitNanos(self, long: int) -> int: ...
    def awaitUninterruptibly(self) -> None: ...
    def awaitUntil(self, date: java.util.Date) -> bool: ...
    def signal(self) -> None: ...
    def signalAll(self) -> None: ...

class Lock(java.lang.Object):
    """
    public interface Lock
    
        :code:`Lock` implementations provide more extensive locking operations than can be obtained using :code:`synchronized`
        methods and statements. They allow more flexible structuring, may have quite different properties, and may support
        multiple associated :class:`~java.util.concurrent.locks.Condition` objects.
    
        A lock is a tool for controlling access to a shared resource by multiple threads. Commonly, a lock provides exclusive
        access to a shared resource: only one thread at a time can acquire the lock and all access to the shared resource
        requires that the lock be acquired first. However, some locks may allow concurrent access to a shared resource, such as
        the read lock of a :class:`~java.util.concurrent.locks.ReadWriteLock`.
    
        The use of :code:`synchronized` methods or statements provides access to the implicit monitor lock associated with every
        object, but forces all lock acquisition and release to occur in a block-structured way: when multiple locks are acquired
        they must be released in the opposite order, and all locks must be released in the same lexical scope in which they were
        acquired.
    
        While the scoping mechanism for :code:`synchronized` methods and statements makes it much easier to program with monitor
        locks, and helps avoid many common programming errors involving locks, there are occasions where you need to work with
        locks in a more flexible way. For example, some algorithms for traversing concurrently accessed data structures require
        the use of "hand-over-hand" or "chain locking": you acquire the lock of node A, then node B, then release A and acquire
        C, then release B and acquire D and so on. Implementations of the :code:`Lock` interface enable the use of such
        techniques by allowing a lock to be acquired and released in different scopes, and allowing multiple locks to be
        acquired and released in any order.
    
        With this increased flexibility comes additional responsibility. The absence of block-structured locking removes the
        automatic release of locks that occurs with :code:`synchronized` methods and statements. In most cases, the following
        idiom should be used:
    
        .. code-block: java
        
         
         Lock l = ...;
         l.lock();
         try {
           // access the resource protected by this lock
         } finally {
           l.unlock();
         }
        When locking and unlocking occur in different scopes, care must be taken to ensure that all code that is executed while
        the lock is held is protected by try-finally or try-catch to ensure that the lock is released when necessary.
    
        :code:`Lock` implementations provide additional functionality over the use of :code:`synchronized` methods and
        statements by providing a non-blocking attempt to acquire a lock (:meth:`~java.util.concurrent.locks.Lock.tryLock`), an
        attempt to acquire the lock that can be interrupted (:meth:`~java.util.concurrent.locks.Lock.lockInterruptibly`, and an
        attempt to acquire the lock that can timeout (:meth:`~java.util.concurrent.locks.Lock.tryLock`).
    
        A :code:`Lock` class can also provide behavior and semantics that is quite different from that of the implicit monitor
        lock, such as guaranteed ordering, non-reentrant usage, or deadlock detection. If an implementation provides such
        specialized semantics then the implementation must document those semantics.
    
        Note that :code:`Lock` instances are just normal objects and can themselves be used as the target in a
        :code:`synchronized` statement. Acquiring the monitor lock of a :code:`Lock` instance has no specified relationship with
        invoking any of the :meth:`~java.util.concurrent.locks.Lock.lock` methods of that instance. It is recommended that to
        avoid confusion you never use :code:`Lock` instances in this way, except within their own implementation.
    
        Except where noted, passing a :code:`null` value for any parameter will result in a
        :class:`~java.lang.NullPointerException` being thrown.
    
        Memory Synchronization
    ----------------------
    
    
        All :code:`Lock` implementations *must* enforce the same memory synchronization semantics as provided by the built-in
        monitor lock, as described in :meth:`~java.util.concurrent.locks.https:.docs.oracle.com.javase.specs.jls.se8.html.jls`:
    
          - A successful :code:`lock` operation has the same memory synchronization effects as a successful *Lock* action.
          - A successful :code:`unlock` operation has the same memory synchronization effects as a successful *Unlock* action.
    
        Unsuccessful locking and unlocking operations, and reentrant locking/unlocking operations, do not require any memory
        synchronization effects.
    
        Implementation Considerations
    -----------------------------
    
    
        The three forms of lock acquisition (interruptible, non-interruptible, and timed) may differ in their performance
        characteristics, ordering guarantees, or other implementation qualities. Further, the ability to interrupt the *ongoing*
        acquisition of a lock may not be available in a given :code:`Lock` class. Consequently, an implementation is not
        required to define exactly the same guarantees or semantics for all three forms of lock acquisition, nor is it required
        to support interruption of an ongoing lock acquisition. An implementation is required to clearly document the semantics
        and guarantees provided by each of the locking methods. It must also obey the interruption semantics as defined in this
        interface, to the extent that interruption of lock acquisition is supported: which is either totally, or only on method
        entry.
    
        As interruption generally implies cancellation, and checks for interruption are often infrequent, an implementation can
        favor responding to an interrupt over normal method return. This is true even if it can be shown that the interrupt
        occurred after another action may have unblocked the thread. An implementation should document this behavior.
    
        Since:
            1.5
    
        Also see:
            :class:`~java.util.concurrent.locks.ReentrantLock`, :class:`~java.util.concurrent.locks.Condition`,
            :class:`~java.util.concurrent.locks.ReadWriteLock`
    
    
    """
    def lock(self) -> None: ...
    def lockInterruptibly(self) -> None: ...
    def newCondition(self) -> Condition: ...
    @typing.overload
    def tryLock(self) -> bool: ...
    @typing.overload
    def tryLock(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> bool: ...
    def unlock(self) -> None: ...

class LockSupport(java.lang.Object):
    """
    Java class 'java.util.concurrent.locks.LockSupport'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    def getBlocker(cls, thread: java.lang.Thread) -> typing.Any: ...
    @classmethod
    @typing.overload
    def park(cls) -> None: ...
    @classmethod
    @typing.overload
    def park(cls, object: typing.Any) -> None: ...
    @classmethod
    @typing.overload
    def parkNanos(cls, object: typing.Any, long: int) -> None: ...
    @classmethod
    @typing.overload
    def parkNanos(cls, long: int) -> None: ...
    @classmethod
    @typing.overload
    def parkUntil(cls, object: typing.Any, long: int) -> None: ...
    @classmethod
    @typing.overload
    def parkUntil(cls, long: int) -> None: ...
    @classmethod
    def unpark(cls, thread: java.lang.Thread) -> None: ...

class ReadWriteLock(java.lang.Object):
    """
    public interface ReadWriteLock
    
        A :code:`ReadWriteLock` maintains a pair of associated :class:`~java.util.concurrent.locks.Lock`, one for read-only
        operations and one for writing. The :meth:`~java.util.concurrent.locks.ReadWriteLock.readLock` may be held
        simultaneously by multiple reader threads, so long as there are no writers. The
        :meth:`~java.util.concurrent.locks.ReadWriteLock.writeLock` is exclusive.
    
        All :code:`ReadWriteLock` implementations must guarantee that the memory synchronization effects of :code:`writeLock`
        operations (as specified in the :class:`~java.util.concurrent.locks.Lock` interface) also hold with respect to the
        associated :code:`readLock`. That is, a thread successfully acquiring the read lock will see all updates made upon
        previous release of the write lock.
    
        A read-write lock allows for a greater level of concurrency in accessing shared data than that permitted by a mutual
        exclusion lock. It exploits the fact that while only a single thread at a time (a *writer* thread) can modify the shared
        data, in many cases any number of threads can concurrently read the data (hence *reader* threads). In theory, the
        increase in concurrency permitted by the use of a read-write lock will lead to performance improvements over the use of
        a mutual exclusion lock. In practice this increase in concurrency will only be fully realized on a multi-processor, and
        then only if the access patterns for the shared data are suitable.
    
        Whether or not a read-write lock will improve performance over the use of a mutual exclusion lock depends on the
        frequency that the data is read compared to being modified, the duration of the read and write operations, and the
        contention for the data - that is, the number of threads that will try to read or write the data at the same time. For
        example, a collection that is initially populated with data and thereafter infrequently modified, while being frequently
        searched (such as a directory of some kind) is an ideal candidate for the use of a read-write lock. However, if updates
        become frequent then the data spends most of its time being exclusively locked and there is little, if any increase in
        concurrency. Further, if the read operations are too short the overhead of the read-write lock implementation (which is
        inherently more complex than a mutual exclusion lock) can dominate the execution cost, particularly as many read-write
        lock implementations still serialize all threads through a small section of code. Ultimately, only profiling and
        measurement will establish whether the use of a read-write lock is suitable for your application.
    
        Although the basic operation of a read-write lock is straight-forward, there are many policy decisions that an
        implementation must make, which may affect the effectiveness of the read-write lock in a given application. Examples of
        these policies include:
    
          - Determining whether to grant the read lock or the write lock, when both readers and writers are waiting, at the time
            that a writer releases the write lock. Writer preference is common, as writes are expected to be short and infrequent.
            Reader preference is less common as it can lead to lengthy delays for a write if the readers are frequent and long-lived
            as expected. Fair, or "in-order" implementations are also possible.
          - Determining whether readers that request the read lock while a reader is active and a writer is waiting, are granted the
            read lock. Preference to the reader can delay the writer indefinitely, while preference to the writer can reduce the
            potential for concurrency.
          - Determining whether the locks are reentrant: can a thread with the write lock reacquire it? Can it acquire a read lock
            while holding the write lock? Is the read lock itself reentrant?
          - Can the write lock be downgraded to a read lock without allowing an intervening writer? Can a read lock be upgraded to a
            write lock, in preference to other waiting readers or writers?
    
        You should consider all of these things when evaluating the suitability of a given implementation for your application.
    
        Since:
            1.5
    
        Also see:
            :class:`~java.util.concurrent.locks.ReentrantReadWriteLock`, :class:`~java.util.concurrent.locks.Lock`,
            :class:`~java.util.concurrent.locks.ReentrantLock`
    
    
    """
    def readLock(self) -> Lock: ...
    def writeLock(self) -> Lock: ...

class StampedLock(java.io.Serializable):
    """
    Java class 'java.util.concurrent.locks.StampedLock'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * StampedLock()
    
    """
    def __init__(self): ...
    def asReadLock(self) -> Lock: ...
    def asReadWriteLock(self) -> ReadWriteLock: ...
    def asWriteLock(self) -> Lock: ...
    def getReadLockCount(self) -> int: ...
    @classmethod
    def isLockStamp(cls, long: int) -> bool: ...
    @classmethod
    def isOptimisticReadStamp(cls, long: int) -> bool: ...
    @classmethod
    def isReadLockStamp(cls, long: int) -> bool: ...
    def isReadLocked(self) -> bool: ...
    @classmethod
    def isWriteLockStamp(cls, long: int) -> bool: ...
    def isWriteLocked(self) -> bool: ...
    def readLock(self) -> int: ...
    def readLockInterruptibly(self) -> int: ...
    def toString(self) -> java.lang.String: ...
    def tryConvertToOptimisticRead(self, long: int) -> int: ...
    def tryConvertToReadLock(self, long: int) -> int: ...
    def tryConvertToWriteLock(self, long: int) -> int: ...
    def tryOptimisticRead(self) -> int: ...
    @typing.overload
    def tryReadLock(self) -> int: ...
    @typing.overload
    def tryReadLock(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> int: ...
    def tryUnlockRead(self) -> bool: ...
    def tryUnlockWrite(self) -> bool: ...
    @typing.overload
    def tryWriteLock(self) -> int: ...
    @typing.overload
    def tryWriteLock(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> int: ...
    def unlock(self, long: int) -> None: ...
    def unlockRead(self, long: int) -> None: ...
    def unlockWrite(self, long: int) -> None: ...
    def validate(self, long: int) -> bool: ...
    def writeLock(self) -> int: ...
    def writeLockInterruptibly(self) -> int: ...

class AbstractQueuedLongSynchronizer(AbstractOwnableSynchronizer):
    """
    Java class 'java.util.concurrent.locks.AbstractQueuedLongSynchronizer'
    
        Extends:
            java.util.concurrent.locks.AbstractOwnableSynchronizer
    
        Interfaces:
            java.io.Serializable
    
    """
    def acquire(self, long: int) -> None: ...
    def acquireInterruptibly(self, long: int) -> None: ...
    def acquireShared(self, long: int) -> None: ...
    def acquireSharedInterruptibly(self, long: int) -> None: ...
    def getExclusiveQueuedThreads(self) -> java.util.Collection[java.lang.Thread]: ...
    def getFirstQueuedThread(self) -> java.lang.Thread: ...
    def getQueueLength(self) -> int: ...
    def getQueuedThreads(self) -> java.util.Collection[java.lang.Thread]: ...
    def getSharedQueuedThreads(self) -> java.util.Collection[java.lang.Thread]: ...
    def getWaitQueueLength(self, conditionObject: 'AbstractQueuedLongSynchronizer.ConditionObject') -> int: ...
    def getWaitingThreads(self, conditionObject: 'AbstractQueuedLongSynchronizer.ConditionObject') -> java.util.Collection[java.lang.Thread]: ...
    def hasContended(self) -> bool: ...
    def hasQueuedPredecessors(self) -> bool: ...
    def hasQueuedThreads(self) -> bool: ...
    def hasWaiters(self, conditionObject: 'AbstractQueuedLongSynchronizer.ConditionObject') -> bool: ...
    def isQueued(self, thread: java.lang.Thread) -> bool: ...
    def owns(self, conditionObject: 'AbstractQueuedLongSynchronizer.ConditionObject') -> bool: ...
    def release(self, long: int) -> bool: ...
    def releaseShared(self, long: int) -> bool: ...
    def toString(self) -> java.lang.String: ...
    def tryAcquireNanos(self, long: int, long2: int) -> bool: ...
    def tryAcquireSharedNanos(self, long: int, long2: int) -> bool: ...
    class ConditionObject(Condition, java.io.Serializable):
        """
        Java class 'java.util.concurrent.locks.AbstractQueuedLongSynchronizer$ConditionObject'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.util.concurrent.locks.Condition, java.io.Serializable
        
          Constructors:
            * ConditionObject(java.util.concurrent.locks.AbstractQueuedLongSynchronizer)
        
        """
        def __init__(self, abstractQueuedLongSynchronizer: 'AbstractQueuedLongSynchronizer'): ...
        def awaitNanos(self, long: int) -> int: ...
        def awaitUninterruptibly(self) -> None: ...
        def awaitUntil(self, date: java.util.Date) -> bool: ...
        def signal(self) -> None: ...
        def signalAll(self) -> None: ...

class AbstractQueuedSynchronizer(AbstractOwnableSynchronizer):
    """
    Java class 'java.util.concurrent.locks.AbstractQueuedSynchronizer'
    
        Extends:
            java.util.concurrent.locks.AbstractOwnableSynchronizer
    
        Interfaces:
            java.io.Serializable
    
    """
    def acquire(self, int: int) -> None: ...
    def acquireInterruptibly(self, int: int) -> None: ...
    def acquireShared(self, int: int) -> None: ...
    def acquireSharedInterruptibly(self, int: int) -> None: ...
    def getExclusiveQueuedThreads(self) -> java.util.Collection[java.lang.Thread]: ...
    def getFirstQueuedThread(self) -> java.lang.Thread: ...
    def getQueueLength(self) -> int: ...
    def getQueuedThreads(self) -> java.util.Collection[java.lang.Thread]: ...
    def getSharedQueuedThreads(self) -> java.util.Collection[java.lang.Thread]: ...
    def getWaitQueueLength(self, conditionObject: 'AbstractQueuedSynchronizer.ConditionObject') -> int: ...
    def getWaitingThreads(self, conditionObject: 'AbstractQueuedSynchronizer.ConditionObject') -> java.util.Collection[java.lang.Thread]: ...
    def hasContended(self) -> bool: ...
    def hasQueuedPredecessors(self) -> bool: ...
    def hasQueuedThreads(self) -> bool: ...
    def hasWaiters(self, conditionObject: 'AbstractQueuedSynchronizer.ConditionObject') -> bool: ...
    def isQueued(self, thread: java.lang.Thread) -> bool: ...
    def owns(self, conditionObject: 'AbstractQueuedSynchronizer.ConditionObject') -> bool: ...
    def release(self, int: int) -> bool: ...
    def releaseShared(self, int: int) -> bool: ...
    def toString(self) -> java.lang.String: ...
    def tryAcquireNanos(self, int: int, long: int) -> bool: ...
    def tryAcquireSharedNanos(self, int: int, long: int) -> bool: ...
    class ConditionObject(Condition, java.io.Serializable):
        """
        Java class 'java.util.concurrent.locks.AbstractQueuedSynchronizer$ConditionObject'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.util.concurrent.locks.Condition, java.io.Serializable
        
          Constructors:
            * ConditionObject(java.util.concurrent.locks.AbstractQueuedSynchronizer)
        
        """
        def __init__(self, abstractQueuedSynchronizer: 'AbstractQueuedSynchronizer'): ...
        def awaitNanos(self, long: int) -> int: ...
        def awaitUninterruptibly(self) -> None: ...
        def awaitUntil(self, date: java.util.Date) -> bool: ...
        def signal(self) -> None: ...
        def signalAll(self) -> None: ...

class ReentrantLock(Lock, java.io.Serializable):
    """
    Java class 'java.util.concurrent.locks.ReentrantLock'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.util.concurrent.locks.Lock, java.io.Serializable
    
      Constructors:
        * ReentrantLock()
        * ReentrantLock(boolean)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...
    def getHoldCount(self) -> int: ...
    def getQueueLength(self) -> int: ...
    def getWaitQueueLength(self, condition: Condition) -> int: ...
    def hasQueuedThread(self, thread: java.lang.Thread) -> bool: ...
    def hasQueuedThreads(self) -> bool: ...
    def hasWaiters(self, condition: Condition) -> bool: ...
    def isFair(self) -> bool: ...
    def isHeldByCurrentThread(self) -> bool: ...
    def isLocked(self) -> bool: ...
    def lock(self) -> None: ...
    def lockInterruptibly(self) -> None: ...
    def newCondition(self) -> Condition: ...
    def toString(self) -> java.lang.String: ...
    @typing.overload
    def tryLock(self) -> bool: ...
    @typing.overload
    def tryLock(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> bool: ...
    def unlock(self) -> None: ...

class ReentrantReadWriteLock(ReadWriteLock, java.io.Serializable):
    """
    Java class 'java.util.concurrent.locks.ReentrantReadWriteLock'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.util.concurrent.locks.ReadWriteLock, java.io.Serializable
    
      Constructors:
        * ReentrantReadWriteLock(boolean)
        * ReentrantReadWriteLock()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...
    def getQueueLength(self) -> int: ...
    def getReadHoldCount(self) -> int: ...
    def getReadLockCount(self) -> int: ...
    def getWaitQueueLength(self, condition: Condition) -> int: ...
    def getWriteHoldCount(self) -> int: ...
    def hasQueuedThread(self, thread: java.lang.Thread) -> bool: ...
    def hasQueuedThreads(self) -> bool: ...
    def hasWaiters(self, condition: Condition) -> bool: ...
    def isFair(self) -> bool: ...
    def isWriteLocked(self) -> bool: ...
    def isWriteLockedByCurrentThread(self) -> bool: ...
    @typing.overload
    def readLock(self) -> Lock: ...
    @typing.overload
    def readLock(self) -> 'ReentrantReadWriteLock.ReadLock': ...
    def toString(self) -> java.lang.String: ...
    @typing.overload
    def writeLock(self) -> Lock: ...
    @typing.overload
    def writeLock(self) -> 'ReentrantReadWriteLock.WriteLock': ...
    class ReadLock(Lock, java.io.Serializable):
        """
        Java class 'java.util.concurrent.locks.ReentrantReadWriteLock$ReadLock'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.util.concurrent.locks.Lock, java.io.Serializable
        
        """
        def lock(self) -> None: ...
        def lockInterruptibly(self) -> None: ...
        def newCondition(self) -> Condition: ...
        def toString(self) -> java.lang.String: ...
        @typing.overload
        def tryLock(self) -> bool: ...
        @typing.overload
        def tryLock(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> bool: ...
        def unlock(self) -> None: ...
    class WriteLock(Lock, java.io.Serializable):
        """
        Java class 'java.util.concurrent.locks.ReentrantReadWriteLock$WriteLock'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.util.concurrent.locks.Lock, java.io.Serializable
        
        """
        def getHoldCount(self) -> int: ...
        def isHeldByCurrentThread(self) -> bool: ...
        def lock(self) -> None: ...
        def lockInterruptibly(self) -> None: ...
        def newCondition(self) -> Condition: ...
        def toString(self) -> java.lang.String: ...
        @typing.overload
        def tryLock(self) -> bool: ...
        @typing.overload
        def tryLock(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> bool: ...
        def unlock(self) -> None: ...
