
function _defineProperty(obj, key, value) {if (key in obj) {Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true });} else {obj[key] = value;}return obj;} // Check out the final version LIVE on Github!
// http://pizzabotdemo.netlify.com

class App extends React.Component {

  constructor(props) {
    super(props);_defineProperty(this, "updateTimer",

    () => {

      this.setState({
        overlayStatus: 'active' });


      // var currentMinutes = this.state.timer.minutes * 60;
      // var currentSeconds = this.state.timer.seconds;

      // this.setState({
      //     timer: {
      //         minutes: currentMinutes,
      //         seconds: currentSeconds,
      //     }
      // })

      // console.log('minutes =>', minutes, 'seconds =>', seconds)


    });_defineProperty(this, "updateUserMessages",

    newMessage => {

      // Create a new array from current user messages
      var updatedUserMessagesArr = this.state.userMessages;

      // Create a new array from current bot messages
      var updatedBotMessagesArr = this.state.botMessages;

      // Render user message and bot's loading message
      this.setState({
        userMessages: updatedUserMessagesArr.concat(newMessage),
        botLoading: true });


      // Get the request to DialogFlow in a nice little package with the user's message
      var request = new Request('https://api.dialogflow.com/v1/query?v=20150910&contexts=shop&lang=en&query=' + newMessage + '&sessionId=12345', {
        headers: new Headers({
          "Authorization": "Bearer 64ea0bb39e4d434eb25d7008482e4afe" // Replace this with your own API keys to prevent chatbot from breaking...
        }) });


      // Send the request via fetch
      fetch(request).
      then(response => response.json()).
      then(json => {
        console.log('BOT RESPONSE:', json.result.fulfillment.speech);

        // End conversation and show animation once user hits end flag in API
        var endConvoFlag = json.result.metadata.endConversation;
        if (endConvoFlag !== undefined || endConvoFlag === true) {
          this.updateTimer();
        }

        var botResponse = json.result.fulfillment.speech;

        // Update state with both user and bot's latest messages
        this.setState({
          botMessages: updatedBotMessagesArr.concat(botResponse),
          botLoading: false });



      }).
      catch(function (error) {
        console.log('ERROR =>', error);
      });
    });this.state = { userMessages: [], botMessages: [], botGreeting: 'Hello! What do you need help with?', botLoading: false, overlayStatus: '', timer: { minutes: 30, seconds: 0 } };}

  showMessages() {

    var userConvo = this.state.userMessages;

    // Show initial bot welcome message
    if (this.state.userMessages.length === 0) {
      return;
    }

    var updatedConvo = userConvo.map((data, index) => {

      var botResponse = this.state.botMessages[index];

      return (
        React.createElement("div", { className: "conversation-pair", key: 'convo' + index },
        React.createElement(UserBubble, { message: data, key: 'u' + index }),
        React.createElement(BotBubble, { message: botResponse, key: 'b' + index })));


    });

    return updatedConvo;

  }

  render() {

    var link = React.createElement('a', {href: 'http://127.0.0.1:5000/accepted'}, "Back")

    return (
      React.createElement("div", { id: "app-container" },

      React.createElement("div", {className: "back-button"}, link),

      React.createElement("div", { className: "convo-container" },
      React.createElement(BotBubble, { message: this.state.botGreeting, key: "bot-00" }),
      this.showMessages()),

      React.createElement(UserInput, { userMessage: this.state.userMessage, updateUserMessages: this.updateUserMessages })));



  }}


class UserBubble extends React.Component {

  render() {

    return (
      React.createElement("div", { className: "user-message-container" },
      React.createElement("div", { className: "chat-bubble user" }, this.props.message)));


  }}



class BotBubble extends React.Component {constructor(...args) {super(...args);_defineProperty(this, "componentDidMount",

    () => {

      var lastBubble = this.refs.chatBubble;
      lastBubble.scrollIntoView(true);
    });}

  render() {

    return (
      React.createElement("div", { className: "bot-message-container" },
      React.createElement("div", { className: "img-avatar-container" },
      React.createElement("img", { className: "bot-avatar", src: "/chatbot.jpg", alt: "bot" })),


      React.createElement("div", { className: "chat-bubble bot", ref: "chatBubble" }, this.props.message ? this.props.message : '...')));


  }}


class UserInput extends React.Component {constructor(...args) {super(...args);_defineProperty(this, "handleChange",

    event => {

      if (event.key === 'Enter') {
        var userInput = event.target.value;

        // update state on parent component
        this.props.updateUserMessages(userInput);
        event.target.value = '';
      }
    });}

  render() {
    return (
      React.createElement("div", { className: "input-container" },
      React.createElement("input", { id: "chat", type: "text", onKeyPress: this.handleChange, placeholder: "type in your text to chat" })));



  }}


ReactDOM.render(React.createElement(App, null), document.getElementById('root'));
