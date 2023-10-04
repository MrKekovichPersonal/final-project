<script setup>

import {onMounted, ref} from "vue";

const editMode = ref(false)

// employees fields
const fullName = ref("")
const phoneNumber = ref("")
const emailAddress = ref("")
const salary = ref("")

async function switchEditMode() {
  props.employee['full_name'] = fullName.value
  props.employee['phone_number'] = phoneNumber.value
  props.employee['email_address'] = emailAddress.value
  props.employee['salary'] = salary.value
  editMode.value = !editMode.value
}

async function editEmployee() {
  await validateInput()
  fullName.value = props.employee['full_name']
  phoneNumber.value = props.employee['phone_number']
  emailAddress.value = props.employee['email_address']
  salary.value = props.employee['salary']
  // TODO: add eel call
  editMode.value = false
}

async function validateInput() {
  // TODO: add validation
}

async function deleteEmployee() {
  // TODO: add eel call
}

const props = defineProps({
  employee: Object
})
onMounted(() => {
  fullName.value = props.employee['full_name']
  phoneNumber.value = props.employee['phone_number']
  emailAddress.value = props.employee['email_address']
  salary.value = props.employee['salary']
})
</script>

<template>
  <!--
  employee['employee_id']
  employee['full_name']
  employee['phone_number']
  employee['email_address']
  employee['salary']
  -->
  <th scope="row">
    {{ employee['employee_id'] }}
  </th>
  <th>
    <input class="form-control" v-if="editMode" type="text" v-model="employee['full_name']">
    <input v-else class="form-control disabled" readonly v-model="fullName">
  </th>
  <th>
    <input class="form-control" v-if="editMode" type="tel" v-model="employee['phone_number']">
    <input v-else class="form-control disabled" readonly v-model="phoneNumber">
  </th>
  <th>
    <input class="form-control" v-if="editMode" type="email" v-model="employee['email_address']">
    <input v-else class="form-control disabled" readonly v-model="emailAddress">
  </th>
  <th>
    <input class="form-control" v-if="editMode" type="text" v-model="employee['salary']">
    <input v-else class="form-control disabled" readonly v-model="salary">
  </th>
  <template v-if="!editMode">
    <th class="btn-primary" @click="switchEditMode">
      edit
    </th>
    <th class="btn-danger">
      delete
    </th>
  </template>
  <template v-else>
    <th class="btn-success" @click="editEmployee">
      save
    </th>
    <th class="btn-secondary" @click="switchEditMode">
      cancel
    </th>
  </template>
</template>

<style scoped>
.employee {
  display: flex;
}

</style>