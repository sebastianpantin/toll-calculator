import { Box, Container, Text } from "@chakra-ui/react"
import { createFileRoute } from "@tanstack/react-router"

export const Route = createFileRoute("/__layout/overview")({
    component: Overview,
})

function Overview() {
    return (
        <>
            <Container maxW="full">
                <Box pt={12} m={4}>
                    <Text fontSize="2xl">Overview</Text>
                </Box>
            </Container>
        </>
    )
}
