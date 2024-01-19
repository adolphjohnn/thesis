function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function getTime() {
  let today = new Date();
  hours = today.getHours();
  minutes = today.getMinutes();

  if (hours < 10) {
      hours = "0" + hours;
  }

  if (minutes < 10) {
      minutes = "0" + minutes;
  }

  let time = hours + ":" + minutes;
  return time;
}



let form = document.querySelector(".submit-form")
let input = document.querySelector("#textInput")

let heading = document.querySelector("#main-header")
let bot_container = document.querySelector(".bot-feature-container")
let container = document.querySelector("#chatbox")
let modalbody = document.querySelector("#modalbody")
let spinner = document.querySelector(".spinner-main")

form.addEventListener("submit", submitForm)

function heartButton() {
  let message = input.value
  const data = { msg : message };
  postJSON(data);
}


function sendButton1() {
  modal.style.display = "block";
}


async function postJSON(data) {
    spinner.style.display = "flex"
    const url = "/get-value"
    try {
      const response = await fetch(url, {
        method: "POST", // or 'PUT'
        headers: {
          "Content-Type": "application/json",
          'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data),
      });
  
      let time = getTime();

      $("#chat-timestamp").append(time);
      const result = await response.json();
      heading.style.display = "none"
      bot_container.style.display = "none"
      spinner.style.display = "none"

      container.innerHTML += `<div class="chat-container1">
      <div class="user-chat-container style="text-align: right;"">

          <p id="botStarterMessage" style="color:blue; text-align: right;" class="botText">${result.msg}</span></p>
          <div class="user-pic"><i class="fa-solid fa-circle-user"></i></div>

      </div>
      <div class="bot-chat-container">


            <div class="user-pic"><i class="fa-solid fa-circle-user"></i></div>
            <p id="botStarterMessage1" style="color:blue;" class="botText">${result.res}</span></p>

  </div>

  </div>

  `
  document.getElementById("textInput").value = ""
  document.getElementById("textInput").innerText=""
  input.value = ""
      console.log("Success:", result);

    } catch (error) {
      console.error("Error:", error);
    }
  }
  
  

function submitForm(e){
    e.preventDefault()
    let message = input.value
    const data = { msg : message };
    postJSON(data);

}


// Press enter to send a message
$("#textInput").keypress(function (e) {
  if (e.which == 13) {
    let message = input.value
    const data = { msg : message };
    postJSON(data);
  
  }
});