import { Box, Flex, Icon, Text, useColorModeValue, Link } from "@chakra-ui/react"
import { FiHome } from "react-icons/fi"
import { FaCashRegister } from "react-icons/fa"
import { VscGraphLine } from "react-icons/vsc"

const items = [
    { icon: FiHome, title: "Home", path: "/" },
    { icon: FaCashRegister, title: "Register", path: "/register" },
    { icon: VscGraphLine, title: "Overview", path: "/overview" },
]

export const Sidebar = () => {
    const bgColor = useColorModeValue("ui.light", "ui.dark")
    const secBgColor = useColorModeValue("ui.secondary", "ui.darkSlate")
    return (
        <Box bg={bgColor} p={3} h="100vh" position="sticky" top="0" display={{ base: "none", md: "flex" }}>
            <Flex flexDir="column" justify="space-between" bg={secBgColor} p={4} borderRadius={12}>
                <Box>
                    <SidebarItems />
                </Box>
            </Flex>
        </Box>
    )
}

interface SidebarItemsProps {
    onClose?: () => void
}

const SidebarItems = ({ onClose }: SidebarItemsProps) => {
    const textColor = useColorModeValue("ui.main", "ui.light")

    const listItems = items.map(({ icon, title, path }) => (
        <Flex w="100%" p={2} key={title} color={textColor} onClick={onClose}>
            <Icon as={icon} alignSelf="center" />
            <Link href={path}>
                <Text ml={2}>{title}</Text>
            </Link>
        </Flex>
    ))

    return (
        <>
            <Box>{listItems}</Box>
        </>
    )
}
