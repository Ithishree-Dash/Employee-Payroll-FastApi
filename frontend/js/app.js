
const API="https://employee-payroll-fast-oyrje46w6-ithishree-dashs-projects.vercel.app";

async function addFT(){
 await fetch(API+"/employees/fulltime",{
  method:"POST",
  headers:{"Content-Type":"application/json"},
  body:JSON.stringify({
   name:ftname.value,
   id:Number(ftid.value),
   monthlySalary:Number(ftsalary.value)
  })
 });
 loadEmployees();
}

async function addPT(){
 await fetch(API+"/employees/parttime",{
  method:"POST",
  headers:{"Content-Type":"application/json"},
  body:JSON.stringify({
   name:ptname.value,
   id:Number(ptid.value),
   hoursWorked:Number(hours.value),
   hourlyRate:Number(rate.value)
  })
 });
 loadEmployees();
}

async function delEmp(id){
 await fetch(API+"/employees/"+id,{method:"DELETE"});
 loadEmployees();
}

async function loadEmployees(){
 const data=await (await fetch(API+"/employees")).json();
 let html="";
 data.forEach(e=>{
  html+=`<tr>
  <td>${e.id}</td>
  <td>${e.name}</td>
  <td>${e.type}</td>
  <td>₹${e.salary}</td>
  <td><button class="delete-btn" onclick="delEmp(${e.id})">Delete</button></td>
  </tr>`;
 });
 document.querySelector("#tbl tbody").innerHTML=html;
}
loadEmployees();
