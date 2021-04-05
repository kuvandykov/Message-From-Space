<template>
    <div class="messages">
        <message v-for="message in messages" :key="message.id"
        :text="message.text"
        :id="message.id"
        :read="message.read"/>
    </div>

</template>

<script>
    import message from "./message"

    export default {
        name: 'messages',
        components: {
            message
        },
        data() {
            return{
                messages: [],
            }
        },
        async created(){
            var response = await fetch('http://lukura.pythonanywhere.com/api/get_messages/');
            this.messages = await response.json();
            setInterval(() => this.updateMessages(), 10000);
        },
        methods: {
            async updateMessages(){
                var id = 0
                if (this.messages.length != 0){

                    id = this.messages[this.messages.length - 1].id;
                }
                var response = await fetch(`http://lukura.pythonanywhere.com/api/get_messages/?last_id=${id}`);
                if (await response.ok){
                    var new_messages = await response.json();
                    for (let index = 0; index < new_messages.length; index++){
                        this.messages.push(new_messages[index]);
                    }

                }
            },
        }
    }
</script>