package main

import (
	"context"
	"fmt"

	"github.com/ethereum/go-ethereum/ethclient"
)

func main() {
	ctx := context.Background()

	client, err := ethclient.DialContext(ctx, "https://mainnet.infura.io")
	if err != nil {
		fmt.Printf("failed to connect to eth api: %v", err)
		return
	}

	blockNum, err := client.BlockNumber(ctx)
	if err != nil {
		fmt.Printf("failed to get block num: %v", err)
		return
	}

	fmt.Printf("%d", blockNum)
}
