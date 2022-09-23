import Tb from "./Topbar";
// import Grid from "./Grid";
// import Summary from "./Summary";
import Gridnew from "./Gridnew";
import {useState, useEffect} from "react";

function Home() {

  let current_url = window.location.pathname;
  console.log(current_url);
//  let clas = current_url.slice(1,5);
///attendance/8/7/5/

  let cr_id = current_url.slice(12,13);
  let p_id = current_url.slice(14,15);
  let s_id = current_url.slice(16,17);
  console.log(cr_id,p_id,s_id,"qwertyuiop")
  // console.log(s_id);

  // let part2 = current_url.slice(3,4);
  // let part3 = current_url.slice(4,5);
  // let name = part1 + " " + part2 + " " + part3; 
  const classroom_name = "ME3A";
  const classroom_id = cr_id; //get from url
  // const class_room_code = "ME 3 A";
  const [isTogglerAbsent, changePresent] = useState(false)
  //  isTogglerAbsent --> toggler color is green
  function update_Toggler() {
    changePresent(!isTogglerAbsent);
  }
  const initStudentData = [
    { 'rollNumber': '0', 'isPresent': false },
    ];

  /*GETTING DATA FROM BACKEND  i.e fetch */
  const fetchData = () => {
    // http://localhost:8080/classwiseAPI/ME3A/
       return fetch(`http://localhost:8000/classroom/${classroom_id}/`)
      .then((response) =>response.json())
      .then(data => updateStudentData(data));
      // .then(() => console.log("hi"));
    };

  const handleSubmit = () => {
    // e.preventDefault();
    const postable_student_data = {student_data};
    const current_input_reference = {
      "classroom_id": cr_id ,
      "period":p_id,
      "subject_id":s_id,
    }
    var postable_data = Object.assign({},postable_student_data,current_input_reference)
    console.log(postable_student_data);
    
    fetch('http://localhost:8000/attendance/save/',{
      /* input to backend */
      method: 'POST',
      mode: 'cors',
      headers:{ "Content-Type": "application/json"},
      body: JSON.stringify(postable_data)
    }).then(()=>{
      console.log('new postable_student_data added',postable_data);
    })
  }

  const [student_data, updateStudentData] = useState(initStudentData);
  console.log(student_data);
  
  useEffect(() => {
    fetchData();
  // eslint-disable-next-line react-hooks/exhaustive-deps
  },[]);
  const[count, setCount] = useState(0);

  function get_count_presentee(){
    let counter = 0;
    student_data.map((student: { rollNumber: string | any[]; isPresent: boolean; }) => {
      if(student.isPresent === true){
        // console.log(student.isPresent)
        counter ++;
        };
        return {};
      });
    // console.log(counter,"hi")
    return counter;
  }
  get_count_presentee();

  function colorChange(sent_rollNumber: string) {
    const updated_color_data_list = student_data.map(iter => {
      if (iter.rollNumber === sent_rollNumber) {
        const absent = !iter.isPresent
          return{
            ...iter,
            isPresent: absent
          }
      }
      else{
        return iter
      }
    }
    )
    updateStudentData(updated_color_data_list);
    }

    function updaterCount(){
      let current_url = get_count_presentee();
      setCount(current_url)
    }

  return (
    <div>
         <Tb isTogglerAbsent={isTogglerAbsent} update_Toggler={update_Toggler} student_data = {student_data} count={count} classroom={classroom_name}/>
         <Gridnew togglerStatus={isTogglerAbsent} student_data = {student_data} colorChange={colorChange} setCount={updaterCount} handleSubmit = {handleSubmit} />
         {/* <button onClick={handleSubmit}>anything</button> */}
         {/* <Summary /> */}
    </div>
         );
}
export default Home


