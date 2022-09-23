import { useEffect } from "react";
import "./Gridnewstyle.css";

const Gridnew = (props: {
  togglerStatus: boolean;
  student_data: any;
  colorChange: any;
  setCount: any;
  handleSubmit: any;
}) => {
  let listofRollSection: string[] = [];
  function generationSectionalRolls() 
  {
    /* 
    Breaks the students yearwise
    input: props.student_data
    output: Array["18","19","20"]
    */
   
    const no_of_iteration = props.student_data.length;
    let temp = "0K";
    for (let x = 0; x < no_of_iteration; x++) 
    {
      if (props.student_data[x].rollNumber.slice(0, 3) !== temp) 
      {
        // console.log(temp, props.student_data[x].rollNumber.slice(0, 2));
        /* 18K 19K 20K in listofRollSection */
        listofRollSection.push(props.student_data[x].rollNumber.slice(0, 3));
      }
      temp = props.student_data[x].rollNumber.slice(0, 3);
    }
    console.log(listofRollSection)
  }
  // calling function 
  generationSectionalRolls(); 
  
  function StudentStatePresent(presentStatus: boolean) 
  {
    /* input: boolean present status 
    output: green colored grid */
    // function (x) -->  grid-item grid-green-present or grid-item
    return presentStatus ? "grid-item grid-green-present" : "grid-item";
  }
  /* input: boolean present status 
  output: red colored grid */
  function StudentStateAbsent(presentStatus: boolean) {
    // return presentStatus ? "grid-item grid-red-absent" : "grid-item"
    return presentStatus ? "grid-item" : "grid-item grid-red-absent";
  }
 /* updates the count when student_data is altered  */
  useEffect(() => {
    props.setCount();
    printer();
  }, [props.student_data]);
  
  /* Sends data to backend when student_data is altered */
  useEffect(() => {
    props.handleSubmit();
  },
     [props.student_data]);

  /* console printing of student data  */
  function printer(){
    console.log(props.student_data)
  };
  
  return (
    <div>
      {/* <h1>{props.togglerStatus ? "true" : "false"}</h1> */}
      {
       listofRollSection.map((each_rollno_series) => 
       {
        return (
          <div className="year_box">
            {/* Prints the roll number headers 18K,19K,20k per se */}
            <h1 id={each_rollno_series}>{each_rollno_series}</h1>
            {/* <parent div container with padding> */}
            <div className="grid-container">
              {props.student_data.map(
                (student: {
                  rollNumber: string | any[];
                  isPresent: boolean;
                }) => {
                  if (student.rollNumber.slice(0, 3) === each_rollno_series) {
                    return (
                      // console.log(props.togglerStatus? "yes": "no")
                      <div
                      /* key is needed to identify, in every return of a mapping function  */
                        key={String(student.rollNumber)}
                        /* changes toggler color */
                        className={
                          props.togglerStatus
                            ? StudentStateAbsent(student.isPresent)
                            : StudentStatePresent(student.isPresent)
                        }
                        onClick={() => {
                          props.colorChange(student.rollNumber); /*changes grid-item color on click*/
                        }} 
                      >   
                        {student.rollNumber.slice(-2)} 
                        {/* to get the last two digits of the roll number */}
                      </div>
                    );
                  }
                }
              )}
            </div>
          </div>
        );
      })}
      <div>
          <button className="submit_grid_btn" onClick={()=>props.handleSubmit()}>Submit</button>  
      </div>
    </div>
  );
};

export default Gridnew;
