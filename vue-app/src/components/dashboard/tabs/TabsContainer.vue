<template>
    <div id="dashboard-wrapper">
        <div class="container">
            <div class="row">
                <div class="col">
                    <ul class="nav nav-tabs" id="accountsTablist">
                        <li class="nav-item add">
                            <button class="nav-link btn btn-success" id="newAccountItem" type="button">+</button>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="tab-content" id="tabContent"></div>
            <!-- <script>
                initAccounts();
            </script> -->
        </div>
    </div>
</template>

<script>
export default {
    name: "TabsContainer",
    mouted(){

    }

}
</script>