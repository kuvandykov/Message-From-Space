<template>
    <span class="message d-flex flex-wrap">
        <p class="flex-grow-1"> {{ text }}</p>
        <button onclick="style.display='none'" type="button flex-grow-0" @click="MessageReaded"> Прочитано </button>
    </span>
</template>

<script>
    export default {
        name: 'message',
        props: ['id', 'text', 'read'],
        data() {
            return {
                data: {},
            }
        },
        methods: {
            async MessageReaded(){
                    await fetch(`http://localhost:8000/api/mark_read/?id=${this.id}`, {
                    method: 'patch',
                }
                )}
        }
    }
</script>