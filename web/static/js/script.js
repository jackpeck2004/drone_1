inputDiv = document.querySelector('.input');
commandsDiv = document.querySelector('.previous_commands');
command = document.getElementById('command');
button = document.getElementById('button');
commands = document.querySelector('.commands');
startButtonDiv = document.querySelector('#start');
startButton = document.querySelector('#start>input[type=button]');

const sendCommand = command => {
  axios.get('/command/' + command);
};

startButton.addEventListener('click', () => {
  //alert('hello');
  sendCommand('command');
  inputDiv.style.display = 'block';
  commandsDiv.style.display = 'block';
  startButtonDiv.style.display = 'none';
  // setInterval(() => {
  //   sendCommand('battery?');
  // }, 5000);
});

const addElement = element => {
  let ul = document.getElementById('list');
  let li = document.createElement('li');
  li.appendChild(document.createTextNode(element));
  ul.appendChild(li);
};

button.addEventListener('click', () => {
  sendInput();
});

const sendInput = () => {
  if (command.value != "" || command.value !== " ") {
    sendCommand(command.value);
    commands.innerHTMl = "<p>" + command.value + "</p><br />";
    addElement(command.value);
    command.value = "";
  }
}

command.addEventListener('keypress', e => {
  if(e.key === 'Enter') {
    sendInput();
  }
});
