import { Box, Container, Text } from "@chakra-ui/react"
import { createFileRoute } from "@tanstack/react-router"

export const Route = createFileRoute("/__layout/")({
    component: Home,
})

function Home() {
    return (
        <>
            <Container maxW="full">
                <Box pt={12} m={4}>
                    <Text fontSize="2xl">Home</Text>
                </Box>
            </Container>
        </>
    )
}
