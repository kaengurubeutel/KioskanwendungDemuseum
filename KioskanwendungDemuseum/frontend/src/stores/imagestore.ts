import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const imagestore = defineStore('counter', {
  state: () => ({ scribble: Blob, result: Blob, promptdata:Object}),

})