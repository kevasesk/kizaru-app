<template>
    <li class="nav-item username" id="${id}" data-username="${username}">
        <button class="nav-link block-head" data-bs-toggle="tab" data-bs-target="${target}" type="button" data-id="${id}" data-child-id="${childId}">
            <img class="profile-pic-small" data-target="${target}" src="${img}">
            <span>${usernameData}</snap>
        </button>
        <button class="btn btn-danger close" data-target="${target}" type="button" onclick="closeTab('${id}', '${childId}')">X</button>
    </li>
</template>

<script>
export default {
 name: "TabItem",
}
</script>

<style>

</style>