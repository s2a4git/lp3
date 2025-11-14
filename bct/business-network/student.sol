// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {

    // -------- Structure --------
    struct Student {
        string name;
        uint roll;
        uint marks;
    }

    // -------- Array of Students --------
    Student[] public students;

    // Add a student
    function addStudent(string memory _name, uint _roll, uint _marks) public {
        students.push(Student(_name, _roll, _marks));
    }

    // Get student by index
    function getStudent(uint index) public view returns(string memory, uint, uint) {
        Student memory s = students[index];
        return (s.name, s.roll, s.marks);
    }

    // -------- Fallback Function --------
    // Runs when someone sends ETH or calls invalid function
    fallback() external payable {
        // Simply accept ETH
    }

    // Receive ether directly
    receive() external payable {}
}
