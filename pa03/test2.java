import java.util.concurrent.locks.ReentrantLock;
public class RWLock{
 // Synchronization variables
private final Lock lock=new ReentrantLock();
private final Condition readGo=lock.newCondition();
private final Condition writeGo=lock.newCondition();
 // State variables
 private int activeReaders=0;
 private int activeWriters=0;
 private int waitingReaders=0;
 private int waitingWriters=0;
// Read waits if any active write
private bool readShouldWait(){
    return (activeWriters>0);
}
// Write waits for active read or write
private bool writeShouldWait(){
    return(activeWriters>0||activeReaders>0);
}
public void startRead(){
    lock.lock();
    try{
        waitingReaders++;
        while(readShouldWait()){
        lock.readGo.await();
        }
        waitingReaders--;
        activeReaders++;
    }finally{
        lock.unlock()
    }
}
   // Done reading. If no other active reads, a write may proceed.
public void doneRead(){
    lock.lock();
    try{
        activeReaders--;
        if (activeReaders==0 && waitingWriters>0){
            lock.writeGo.signal();
        }
        else if(activeReaders==0 && waitingReaders>0){
            lock.readGo.signal();
        }
    }finally{
        lock.unlock()
    }
}
// Wait until no active read or write then proceed.
public void startWrite(){
    lock.lock();
    try{
        waitingWriters++;
        while (writeShouldWait()){
        lock.writeGo.await();
        }
        waitingWriters--;
        activeWriters++;
    }finally{
        lock.unlock()
    }
}
   // Done writing. A waiting write or read may proceed.
   void
   public void doneWrite(){
    lock.lock();
    try{
        activeWriters--;
        assert(activeWriters==0);
        if(waitingWriters > 0){
        lock.writeGo.signal();
        }
        else if(waitingReaders>0){
        lock.readGo.signalAll();
        }
    }finally{
        lock.unlock()
    }
}
}