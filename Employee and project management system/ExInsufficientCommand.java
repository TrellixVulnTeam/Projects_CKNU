public class ExInsufficientCommand extends Exception{
    public ExInsufficientCommand() {
        super("Insufficient command arguments.");
    }
    public ExInsufficientCommand(String msg){
        super(msg);
    }
}
