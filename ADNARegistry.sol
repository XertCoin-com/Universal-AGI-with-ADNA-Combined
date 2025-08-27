// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract ADNARegistry {
    event Submitted(bytes32 commit, address signer, uint256 time);
    mapping(bytes32 => address) public submitter;

    function submit(bytes32 commit) external {
        require(submitter[commit] == address(0), "exists");
        submitter[commit] = msg.sender;
        emit Submitted(commit, msg.sender, block.timestamp);
    }
}
