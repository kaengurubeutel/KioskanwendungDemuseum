<template>
    <div :class="keyboardClass"></div>
</template>

<script lang="ts">
import Keyboard from "simple-keyboard";
import "simple-keyboard/build/css/index.css";
import "./keyboard.css";
export default {
    name: "SimpleKeyboard",
    props: {
        keyboardClass: {
            default: "simple-keyboard",
            type: String
        },
        input: {
            type: String
        }
    },
    data: () => ({
        keyboard: null
    }),
    mounted() {
        this.keyboard = new Keyboard(this.keyboardClass, {
            onChange: this.onChange,
            onKeyPress: this.onKeyPress,
            theme: "hg-theme-default hg-layout-default myTheme",
            layout: {
               default: [
                    "` 1 2 3 4 5 6 7 8 9 0 {bksp}",
                    "{tab} q w e r t z u i o p ü",
                    "{lock} a s d f g h j k l ö ä {enter}",
                    "{shift} y x c v b n m , . {shift}",
                    "{space}"
                ],
                shift: [
                    "! 1 2 3 4 5 6 7 8 9 {bksp}",
                    "Q W E R T Z U I O P Ü",
                    '{lock} A S D F G H J K L Ö Ä {enter}',
                    "{shift} Y X C V B N M ; : {shift}",
                    "{space}"
                ]
            },
            buttonTheme: [
                {
                    class: "hg-red",
                    buttons: "! ` 1 2 3 4 5 6 7 8 9 0 Q W E R T Z U I O P Ü A S D F G H J K L Ö Ä Y X C V B N M {space} q w e r t z u i o p ü a s d f g h j k l ö ä y x c v b n m , . ; :"
                },
                {
                    class: "hg-highlight",
                    buttons: "{lock} {shift} {tab} {enter} {bksp}"
                },
               
            ]

        });
    },
    methods: {
        onChange(input) {
            this.$emit("onChange", input);
        },
        onKeyPress(button) {
            this.$emit("onKeyPress", button);

            /**
             * If you want to handle the shift and caps lock buttons
             */
            if (button === "{shift}" || button === "{lock}") this.handleShift();
        },
        handleShift() {
            let currentLayout = this.keyboard.options.layoutName;
            let shiftToggle = currentLayout === "default" ? "shift" : "default";

            this.keyboard.setOptions({
                layoutName: shiftToggle
            });
        }
    },
    watch: {
        input(input) {
            this.keyboard.setInput(input);
        }
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>