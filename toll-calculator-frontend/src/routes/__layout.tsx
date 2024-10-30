import { Flex } from "@chakra-ui/react"
import { Outlet, createFileRoute } from "@tanstack/react-router"

import { Sidebar } from "../components/Sidebar"

export const Route = createFileRoute("/__layout")({
    component: Layout,
})

function Layout() {
    return (
        <Flex maxW="large" h="auto" position="relative">
            <Sidebar />
            <Outlet />
        </Flex>
    )
}
