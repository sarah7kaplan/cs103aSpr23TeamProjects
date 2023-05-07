public class WaitingRoom{
    private int numDogs;
    private int numCats;
    private String state;

    public WaitingRoom(){
        numDogs=0;
        numCats=0;
        state="safe";
    }

    public synchronized void EnterDog(){
        while(!state.equals("dogs")&&!state.equals("safe")){
            try{
                wait();
            }catch(InterruptedException e){
            }
        }
        numDogs++;
        if (state.equals("safe")){
            state = "dogs";
        }
    }

    public synchronized void LeaveDog(){
        numDogs--;
        if(numDogs==0){
            state="safe";
            notifyAll();
        }
    }

    public synchronized void EnterCat(){
        while(!state.equals("cats")&&!state.equals("safe")){
            try{
                wait();
            }catch(InterruptedException e){
            }
        }
        numCats++;
        if(state.equals("safe")){
            state="cats";
        }
    }

    public synchronized void LeaveCat(){
        numCats--;
        if(numCats == 0){
            state = "safe";
            notifyAll();
        }
    }
}