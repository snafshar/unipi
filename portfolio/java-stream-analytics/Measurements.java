import java.util.*;
import java.util.stream.*;
record Measurement(String device,double value){}
public class Measurements {
 public static void main(String[] args){
  var data=List.of(new Measurement("cpu",42),new Measurement("cpu",58),new Measurement("ram",70));
  var averages=data.stream().collect(Collectors.groupingBy(Measurement::device,Collectors.averagingDouble(Measurement::value)));
  System.out.println(averages);
 }
}
