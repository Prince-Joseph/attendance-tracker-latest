import "./mocktop.css";
// import ReactDOM from "react-dom";
import { useState } from "react";

const Tb = (props:{isTogglerAbsent:boolean,update_Toggler:any, student_data:any, count:number, classroom:string}) => {
  const [rollcount, setRollcount] = useState(0);
  const rollSeries = ["18K81A12", "19K81A12", "20K81A12"];

  function updatingIndex(update_num: number) {
    let temp = update_num + rollcount;
    if (temp > -1) {
      if (temp < rollSeries.length) {
        setRollcount(temp)
      }
    }
  }
  const isTogglerAbsent = props.isTogglerAbsent;
  const update_Toggler = props.update_Toggler; 
  return (
    <div>         
    <div className="top-bar-container">
      <div className="top-bar-left">
        <div>
          <a onClick={() => updatingIndex(-1)} href="#{rou}">
            <button className="arrow-button">
              <img alt="arrow"
                className="arrow-size"
                src="https://img.icons8.com/material/24/000000/chevron-up--v1.png"
              />
            </button>
          </a>
        </div>
        <div className="headerList">
          <button className="K_btn">{rollSeries[rollcount]}</button>
        </div>
        <div>
          <a onClick={() => updatingIndex(1)}>
            <button className="arrow-button">
              <img alt="arrow"
                className="arrow-size"
                src="https://img.icons8.com/material/24/000000/chevron-down--v1.png"
              />
            </button>
          </a>
        </div>
      </div>

      <div className="top-bar-right">
        <div>
          <button className="section_name">
            <strong> {props.classroom}</strong>
          </button>
        </div>

        <div
          className={isTogglerAbsent ? "A-buttons-lastlayer" : "PA-buttons-lastlayer"}>
          <div>
            <div className="PA-buttons-whitelayer">
              <button className={isTogglerAbsent ? "Present_button" : "Present_button bg_change_green"} 
              onClick={() =>update_Toggler()}> P </button>
              <button className={isTogglerAbsent  ? "Absent_button bg_change_red"  : "Absent_button"}
              onClick={() => update_Toggler()}>A </button>
            </div>
          </div>
        </div>

        <div className="top-bar-classstrength">
          <div className="pcount">{props.count}/{props.student_data.length}</div>
          <div >
          <svg width="2" height="19" viewBox="0 0 1 21" fill="none" xmlns="http://www.w3.org/2000/svg">
            <line x1="1" y1="1" x2="0.499999" y2="25" stroke="#A1B6FF" stroke-linecap="round"/>
          </svg>
          </div>
          <div className="a-count">{props.student_data.length - props.count}</div>
        </div>
      </div>
    </div>
  </div>
  );
};
export default Tb;
