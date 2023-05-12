<template>
  <div>
    <div @click="crossOut" :class="{ 'crossed-out': completed }">
      <h3>{{ title }}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WatchListItem',
  props: {
    wish: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      completed: this.wish.completed,
      title: this.wish.title,
    };
  },
  methods: {
    crossOut() {
      this.completed = !this.completed;
    },
  },
};
</script>

<style>
.crossed-out {
  text-decoration: line-through;
}
</style>
